from flask import Flask, request, stream_with_context, Response, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import requests
import os
import traceback

GRADIO_URL = 'https://22e7f9ae135c06371b.gradio.live'
app = Flask(__name__)
CORS(app)

os.environ['FFMPEG_BINARY'] = '/usr/bin/ffmpeg'
os.environ['IMAGEMAGICK_BINARY'] = '/usr/bin/convert'

from googletrans import Translator

from shortGPT.audio.edge_voice_module import EdgeTTSVoiceModule
from shortGPT.config.languages import (EDGE_TTS_VOICENAME_MAPPING, Language)
from shortGPT.engine.eng_content_engine import ContentVideoEngine
from shortGPT.engine.translate_content_engine import ContentVideoEngine as TranslateContentVideoEngine
from shortGPT.gpt import gpt_chat_video
import copy
import sys

REMOTE_URL = ngrok.connect(5000)
print(REMOTE_URL.public_url)
# requests.post('https://server.sidd065.repl.co/set', json={"url":REMOTE_URL.public_url, "key":"shorts"})

translator = Translator()
languages = { 
    "English": ["en", "English", "Helvetica-Bold", Language.ENGLISH],
    "Hindi": ["hi", "Hindi", "Lohit-Devanagari", Language.HINDI],
    "Marathi": ["mr", "Marathi", "Lohit-Devanagari", Language.MARATHI],
    "Bengali": ["bn", "Bengali", "Lohit-Bengali", Language.BENGALI],
    "Gujarati": ["gu", "Gujarati", "Lohit-Gujarati", Language.GUJARATI],
    "Kannada": ["kn", "Kannada", "Lohit-Kannada", Language.KANNADA],
    "Malayalam": ["ml", "Malayalam", "Lohit-Malayalam", Language.MALAYALAM],
    "Tamil": ["ta", "Tamil", "Lohit-Tamil", Language.TAMIL],
    "Telugu": ["te", "Telugu", "Lohit-Telugu", Language.TELUGU],
    "Urdu": ["ur", "Urdu", "KacstDecorative", Language.URDU],
    #"Odia": ["or", "Odia", "Lohit-Odia", Language.],
    #"Assamese": ["as", "Assamese", "Lohit-Assamese", Language.],
    #"Manipuri": ["mni-Mtei", "Manipuri", "Lohit-Bengali", Language.],
    #"Punjabi": ["pa", "Punjabi", "Lohit-Gurmukhi", Language.],
}

abbreviations = {
    "LG ": "Leutenant Governor",
    "Smt ": "Srimati",
    "Shri ": "Shree",
    "PM ": "Prime Minister",
}

@app.route('/ping')
def pong():
    return 'pong'

@app.route('/api/make_video', methods=['POST'])
def make_video():
    script = request.json['script']
    langs = request.json['languages'] #array
    timed_image_urls = None
    video_length = None
    if "imageAssets" in request.json and "length" in request.json:
        timed_image_urls = request.json['imageAssets']
        video_length = request.json['length']
    else:
        urls={}
        keywords = gpt_chat_video.extract_keywords(script)
        videoEngine = ContentVideoEngine(voiceModule=EdgeTTSVoiceModule(EDGE_TTS_VOICENAME_MAPPING[Language.ENGLISH]['male']), 
                                        script=script,
                                        keywords=keywords,
                                        short_type="Me", 
                                        num_images=15, 
                                        background_music_name="Music joakim karud dreams", 
                                        background_video_name="Minecraft jumping circuit",
                                        )
        videoEngine._generateTempAudio()
        videoEngine._speedUpAudio()
        videoEngine._timeCaptions()
        videoEngine._generateImageSearchTerms()
        videoEngine._generateImageUrls()
        #timed_captions = copy.copy(videoEngine._db_timed_captions)
        video_length = copy.copy(videoEngine._db_video_length)
        timed_image_urls = copy.copy(videoEngine._db_timed_image_urls)
        # if 'English' in langs:
        #     os.environ['FONT'] = languages['English'][2]
        #     langs.pop(langs.index('English'))
        #     videoEngine._chooseBackgroundMusic()
        #     videoEngine._chooseBackgroundVideo()
        #     videoEngine._prepareBackgroundAssets()
        #     videoEngine._prepareCustomAssets()
        #     videoEngine._editAndRenderShort()
        #     videoEngine._addMetadata
        #     urls['English'] = f"{GRADIO_URL}/file={videoEngine._db_video_path}"
    
    for lang in langs:
        if lang in languages:
            try:
                os.environ['FONT'] = languages[lang][2]
                os.environ['LANGUAGE'] = languages[lang][1]
                translation = translator.translate(script, dest=languages[lang][0]).text
                voice_module = EdgeTTSVoiceModule(EDGE_TTS_VOICENAME_MAPPING[languages[lang][3]]['male'])
                if languages[lang][3] == Language.ENGLISH:
                    videoEngine = ContentVideoEngine(voiceModule=voice_module, 
                                                script=script,
                                                keywords=keywords,
                                                short_type="Me", 
                                                num_images=15, 
                                                background_music_name="Music joakim karud dreams", 
                                                background_video_name="Minecraft jumping circuit",
                                                language=languages[lang][3],
                                                timed_image_urls=timed_image_urls,
                                                video_length=video_length,
                                                )
                else:
                    videoEngine = TranslateContentVideoEngine(voiceModule=voice_module, 
                                                script=script, 
                                                keywords=keywords,
                                                short_type="Me", 
                                                num_images=10, 
                                                background_music_name="Music joakim karud dreams", 
                                                background_video_name="Minecraft jumping circuit",
                                                language=languages[lang][3],
                                                timed_image_urls=timed_image_urls,
                                                video_length=video_length,
                                                )
                num_steps = videoEngine.get_total_steps()
                progress_counter = 0

                def logger(prog_str):
                    print(progress_counter / (num_steps), f"Creating video - {progress_counter} - {prog_str}")
                videoEngine.set_logger(logger)
                for step_num, step_info in videoEngine.makeContent():
                    print(progress_counter / (num_steps), f"Creating video - {step_info}")
                    progress_counter += 1

                video_path = videoEngine.get_video_output_path()
                file_url_path = f"{GRADIO_URL}/file={video_path}"
                urls[lang] = file_url_path
            except Exception:
                traceback.print_exc()
                print(Exception)
    return urls

@app.route('/api/imageAssets', methods=['POST'])
def imageAssets():
    script = request.json['script']
    keywords = gpt_chat_video.extract_keywords(script)
    videoEngine = ContentVideoEngine(voiceModule=EdgeTTSVoiceModule(EDGE_TTS_VOICENAME_MAPPING[Language.ENGLISH]['male']), 
                                    script=script,
                                    keywords=keywords,
                                    short_type="Me", 
                                    num_images=15, 
                                    background_music_name="Music joakim karud dreams", 
                                    background_video_name="Minecraft jumping circuit",
                                    listImageAssets=True
                                    )
    videoEngine._generateTempAudio()
    videoEngine._speedUpAudio()
    videoEngine._timeCaptions()
    videoEngine._generateImageSearchTerms()
    videoEngine._generateImageUrls()
    imageAssets = videoEngine._db_timed_image_urls
    for i in range(len(imageAssets)):
        for j in range(len(imageAssets[i][1])):
            imageAssets[i][1][j] = f"{GRADIO_URL}/file={imageAssets[i][1][j]}"
    return {"imageAssets": imageAssets, 
            "length": videoEngine._db_video_length}
@app.route('/api/make_script', methods=['POST'])
def make_script():
    input_article = request.json['article']
    for abb in abbreviations.keys():
        if abb in input_article:
            input_article = input_article.replace(abb, abbreviations[abb])
    article = gpt_chat_video.summerize(input_article)
    print("Summary", len(input_article), len(article))
    script = gpt_chat_video.generateScript(article=article, language=Language.ENGLISH)
    return {"script": script}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
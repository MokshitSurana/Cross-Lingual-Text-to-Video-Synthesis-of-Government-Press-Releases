import os
import traceback
from enum import Enum
from googletrans import Translator

from shortGPT.audio.edge_voice_module import EdgeTTSVoiceModule
from shortGPT.audio.eleven_voice_module import ElevenLabsVoiceModule
from shortGPT.config.api_db import ApiKeyManager
from shortGPT.config.languages import (EDGE_TTS_VOICENAME_MAPPING,
                                       ELEVEN_SUPPORTED_LANGUAGES, Language)
from shortGPT.engine.eng_content_engine import ContentVideoEngine
from shortGPT.engine.translate_content_engine import ContentVideoEngine as TranslateContentVideoEngine
from shortGPT.gpt import gpt_chat_video
import copy
import sys

os.environ['FFMPEG_BINARY'] = '/usr/bin/ffmpeg'
os.environ['IMAGEMAGICK_BINARY'] = '/usr/bin/convert'
translator = Translator()


def make_video(script, voice_module, keywords, language, timed_image_urls, video_length, wordCount):
    if language == Language.ENGLISH:
        videoEngine = ContentVideoEngine(voiceModule=voice_module, 
                                     script=script,
                                     keywords=keywords,
                                     short_type="Me", 
                                     num_images=15, 
                                     background_music_name="Music joakim karud dreams", 
                                     background_video_name="Minecraft jumping circuit",
                                     language=language,
                                     timed_image_urls=timed_image_urls,
                                     video_length=video_length,
                                     wordCount=wordCount
                                     )
    else:
        videoEngine = TranslateContentVideoEngine(voiceModule=voice_module, 
                                     script=script, 
                                     keywords=keywords,
                                     short_type="Me", 
                                     num_images=10, 
                                     background_music_name="Music joakim karud dreams", 
                                     background_video_name="Minecraft jumping circuit",
                                     language=language,
                                     timed_image_urls=timed_image_urls,
                                     video_length=video_length,
                                     wordCount=wordCount
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
    print(video_path)
    return video_path

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
    #"Odia": ["or", "Odia", "Lohit-Odia", Language.],
    "Urdu": ["ur", "Urdu", "KacstDecorative", Language.URDU],
    #"Assamese": ["as", "Assamese", "Lohit-Assamese", Language.],
    #"Manipuri": ["mni-Mtei", "Manipuri", "Lohit-Bengali", Language.],
    #"Punjabi": ["pa", "Punjabi", "Lohit-Gurmukhi", Language.],
}

abbreviations = {
    "LG ": "Leutenant Governor",
    "Smt ": "Srimati",
    "Shri ": "Shree",
    "Dr ": "Doctor",
    "PM ": "Prime Minister",
}

#MAKE ENGLISH VIDEO
language= Language.ENGLISH
os.environ['FONT'] = languages['English'][2]
#article = "The President of India, Smt Droupadi Murmu graced and addressed the 10th convocation of Guru Ghasidas Vishwavidyalaya at Bilaspur, Chhattisgarh today (September 1, 2023).\n Speaking on the occasion, the President said that in the modern world, the individuals, institutions and countries should remain ahead in innovation and adopting science & technology for greater progress. She added that for the development of science and technology, appropriate facilities, environment and encouragement are needed. She was happy to note the establishment of Accelerator Based Research Centre at the Guru Ghasidas Vishwavidyalaya. She expressed confidence that this Centre would make its mark through useful research.\n Speaking about the recent success of Chandrayaan-3 mission, the President said that behind that success was not only the ability acquired through years of hard work and dedication, but also the commitment of moving forward without getting discouraged by the obstacles and failures. She urged the Guru Ghasidas Vishwavidyalaya to organize knowledge-enhancing programs and competitions on this historic achievement which would help in developing scientific temper in the society.\n The President said that today India is a respected member of the Nuclear Club and the Space Club on the strength of hard work and talent of our scientists and engineers. She added that the example of ‘High Science’ at ‘Low Cost’ presented by India is appreciated in the country and abroad. She said that by attaining high level competence, students of this university can participate in important decisions of society, state and country. She added that creating opportunities amid challenges is an effective way to achieve success.\n The President said that Guru Ghasidas had spread the immortal and living message that all human beings are equal. About 250 years ago, he advocated for the equality of underprivileged, backward and women. She said that youth can build a better society by following these ideals.\n The President noted that there are a large number of tribals in the area around the Guru Ghasidas Vishwavidyalaya. She said that students can learn life values like sensitivity towards nature, sense of equality in community life and participation of women from the tribal community."
input_article = "Prime Minister met Prime Minister of Canada H.E. Mr. Justin Trudeau on 10th September on the sidelines of the G20 Summit in New Delhi.Prime Minister Trudeau congratulated Prime Minister on the success of India's G20 Presidency.Prime Minister highlighted that India-Canada relations are anchored in shared democratic values, respect for rule of law and strong people-to-people ties. He conveyed our strong concerns about continuing anti-India activities of extremist elements in Canada. They are promoting secessionism and inciting violence against Indian diplomats, damaging diplomtic premises, and threatening the Indian community in Canada and their places of worship. The nexus of such forces with organized crime, drug syndicates and human trafficking should be a concern for Canada as well. It is essential for the two countries to cooperate in dealing with such threats.Prime Minister also mentioned that a relationship based on mutual respect and trust is essential for the progress of India-Canada relationship."
for abb in abbreviations.keys():
    if abb in input_article:
        input_article = input_article.replace(abb, abbreviations[abb])
article = gpt_chat_video.summerize(input_article)
print("Summary", len(input_article), len(article))
# script = gpt_chat_video.generateScript(article=article, language=language.value)
# if input("Correct script?") == "n": sys.exit() 
#script = "The Principal Secretary to the Prime Minister, Doctor PK Mishra, and Leutenant Governor, Delhi Shree Vinay Kumar Saxena conducted an extensive site visit of multiple locations across Delhi to review the preparedness for the upcoming G20 Summit. The review exercise was conducted to ensure that all aspects of the preparation for the Summit were in place on ground as planned. Around 20 locations, including Rajghat, C Hexagon - India Gate, Terminal 3 of Airport and its VIP Lounge Aerocity area, key segments of major roads among others, were visited and reviewed by the Principal Secretary."
script = "The President of India presented National Awards to teachers on Teachers' Day, emphasizing the importance of elementary education and a holistic approach. She called for more recognition of female teachers and highlighted the role of teachers in building the future of the nation. The President stressed the duty of teachers and parents to develop each child's unique abilities and the lasting impact that teachers have on their students."
#script = "Indian Prime Minister met with Canadian Prime Minister Justin Trudeau during the G20 Summit in New Delhi. Trudeau congratulated India on its successful G20 Presidency and both leaders emphasized the importance of their countries' shared democratic values and strong people-to-people ties. However, the Indian Prime Minister also expressed concern over continuing anti-India activities by extremist elements in Canada, including promoting secessionism and inciting violence against Indian diplomats and the Indian community in Canada. He called for cooperation between the two countries in dealing with these threats and emphasized the need for a relationship based on mutual respect and trust."
#script = "The Vice-President, Shri Jagdeep Dhankhar today hailed the successful launch of Aditya-L1, Bharat’s inaugural solar mission and congratulated the scientists and engineers at Indian Space Research Organisation (ISRO) for accomplishing this remarkable feat. Expressing optimism, he emphasized that this mission would greatly deepen our understanding of the solar system. In a X post, the Vice-President said;“The successful launch of Bharat’s first solar mission, Aditya-L1 opens a glorious new chapter in our space journey. I congratulate the scientists and engineers at @isro on this remarkable milestone. This stellar achievement would certainly contribute richly to our understanding of the solar system.”"
keywords = gpt_chat_video.extract_keywords(script)
print("Keywords:",keywords)

videoEngine = ContentVideoEngine(voiceModule=EdgeTTSVoiceModule(EDGE_TTS_VOICENAME_MAPPING[language]['male']), 
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
#videoEngine._chooseBackgroundMusic()
#videoEngine._chooseBackgroundVideo()
#videoEngine._prepareBackgroundAssets
video_length = copy.copy(videoEngine._db_video_length)
timed_image_urls = copy.copy(videoEngine._db_timed_image_urls)
#background_trimmed = copy.copy(videoEngine._db_background_trimmed)
# videoEngine._prepareCustomAssets()
# videoEngine._editAndRenderShort()
# videoEngine._addMetadata
#print(videoEngine._db_video_path)

#lang = "Marathi"
#if True:
for lang in ["English","Gujarati","Tamil","Bengali","Hindi","Marathi"]:
    os.environ['FONT'] = languages[lang][2]
    os.environ['LANGUAGE'] = languages[lang][1]
    language = languages[lang][3]
    wordCount=80
    if lang=="Bengali": wordCount=30
    if lang=="Tamil": wordCount=30
    if lang=="Gujarati": wordCount=30

    #translation = translator.translate(script, dest=languages[lang][0]).text
    try:
        voice_module = EdgeTTSVoiceModule(EDGE_TTS_VOICENAME_MAPPING[language]['male'])
        video_path = make_video(script, voice_module, keywords, language, timed_image_urls, video_length, wordCount)
        #video_path = make_video(translation, voice_module, keywords, language, timed_image_urls, video_length)
        file_name = video_path.split("/")[-1].split("\\")[-1]
        #current_url = self.shortGptUI.share_url+"/" if self.shortGptUI.share else self.shortGptUI.local_url
        #file_url_path = f"{current_url}file={video_path}"
        print("DONE", video_path)
        print("Your video is completed !🎬. Scroll up to open its file location.")
    except Exception as e:
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        error_name = type(e).__name__.capitalize() + " : " + f"{e.args[0]}"
        errorVisible = True
        print("We encountered an error while making this video ❌")
        print("Error", error_name, traceback_str)

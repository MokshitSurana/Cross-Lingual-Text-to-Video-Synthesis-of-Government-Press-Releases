import os
from sys import platform
if platform == "linux":
    os.environ['FFMPEG_BINARY'] = '/usr/bin/ffmpeg'
    os.environ['IMAGEMAGICK_BINARY'] = '/usr/bin/convert'
elif platform == "win32":
    pass

languages = { #0:code, 1:voice, 2:font, 3:fontsize
    "Odia": ["or", "bn", "./assets/fonts/Odia.ttf",43],
    "Assamese": ["as", "bn", "./assets/fonts/Assamese.ttf",43],
    "Punjabi": ["pa", "HINDI", "./assets/fonts/Punjabi.ttf",43],
    #"Manipuri": ["mni-Mtei", "bn", "./assets/fonts/Manipuri.ttf",30],
}

from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip, CompositeAudioClip
from moviepy.video.fx.all import crop, speedx
from moviepy.audio.fx.all import volumex
from audio.voices import VOICENAMES, headers
from audio.tts import generate_voice, strip_silence, parse_webvtt, get_timed_images, adjust_timing
import ffmpeg
from gtts import gTTS
from visual.animations import Zoom
from visual.images import getImagesfromQueries
from visual.transitions import slide_in, slide_out, crossfadein, crossfadeout
from visual.PIL_captions import TextImage, TextImageLegacy
from visual.llm import image_queries, make_script, get_keywords
from googletrans import Translator
from easygoogletranslate import EasyGoogleTranslate
import subprocess, random, time, datetime
from pydub import AudioSegment
import threading
from PIL import Image, ImageFilter
import numpy as np

translator = Translator()
resolution = (608, 1080)

def createAssets(images, sentences, LANGUAGE, header=""):
    while True:
        try:
            if LANGUAGE != "English":
                translations = [translator.translate(sentence, src='en', dest=languages[LANGUAGE][0]) for sentence in sentences]
                sentences = [translation.text for translation in translations]
                pronounce = [translation.pronunciation for translation in translations]
            break
        except Exception as e:
            print(e, "Error in translation. Retrying...")
            time.sleep(5)

    clips = []

    for i in range(len(sentences)):
        # VoiceClip
        while True:
            try:
                if LANGUAGE == 'Punjabi' and pronounce[0]:
                    generate_voice(pronounce[i], f'./tmp_assets/output{LANGUAGE}{i}.wav', VOICENAMES[languages[LANGUAGE][1]]['male'], words_in_cue=0, rate="+15%")
                else:
                    gTTS(sentences[i], lang=languages[LANGUAGE][1], slow=False, lang_check=True).save(f'./tmp_assets/output{LANGUAGE}{i}.wav')
                subprocess.call(['ffmpeg', '-i', f'./tmp_assets/output{LANGUAGE}{i}.wav', f'./tmp_assets/outputffmpeg{LANGUAGE}{i}.wav'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                audio = strip_silence(AudioSegment.from_wav(f'./tmp_assets/outputffmpeg{LANGUAGE}{i}.wav')) + AudioSegment.silent(duration=250)
                audio.export(f'./tmp_assets/output{LANGUAGE}{i}.wav', format='wav')
                os.remove(f'./tmp_assets/outputffmpeg{LANGUAGE}{i}.wav')

                audio_clip = AudioFileClip(f'./tmp_assets/output{LANGUAGE}{i}.wav')
                #if LANGUAGE in ['Odia', 'Assamese', 'Manipuri', 'Punjabi']:
                audio_clip=audio_clip.fx(volumex, factor=1.4).fx(speedx, factor=1.05)
                
                break
            except Exception as e:
                print(e, "Error in voice generation. Retrying...")
                time.sleep(5)
        
        
        clip_duration = audio_clip.duration

        # Base Image
        base = ImageClip('./assets/background.png').set_duration(clip_duration)

        # ImageClip
        image_clip = Zoom(images[i], clip_duration, resolution, mode=random.choice(['in','out']), speed=(random.randint(20, 40)/10), fps=24)
        image_clip = crossfadein(image_clip, 0.5)

        # Background ImageClip
        blurred_image = Image.open(images[i]).filter(ImageFilter.BoxBlur(5))
        blurred_image = ImageClip(np.array(blurred_image)).resize(height=resolution[1]).set_position(('center', 'center')).set_duration(clip_duration)


        # TextClip
        longest_text_clip=0
        text_clip = (ImageClip(TextImageLegacy(sentences[i], font_path=languages[LANGUAGE][2], width=resolution[0]-15, fontsize=languages[LANGUAGE][3], color='#fbd504'))
                        .set_duration(clip_duration))
        text_clip = slide_in(text_clip, 0.2, 'bottom', resolution)
        text_clip = crossfadeout(text_clip, 0.2)
        if text_clip.size[1]>longest_text_clip:
            longest_text_clip=text_clip.size[1]

        text_background = ImageClip('./assets/text_background.png').set_opacity(0.4).set_duration(clip_duration).set_position(('center', resolution[1]-(resolution[1]-700+60)-35))
        
        # Header
        if header in headers.keys():
            header=headers[header]
        else:
            header = './assets/headers/header.png'
        header = ImageClip(header).set_duration(clip_duration).resize(width=resolution[0]-10).set_position(('center', 'top'))     

        final_clip = CompositeVideoClip([base, blurred_image, image_clip, text_background, text_clip, header])
        final_clip = final_clip.set_audio(audio_clip)
        clips.append(final_clip)
    video = concatenate_videoclips(clips, method="chain")
    return video

def renderVideo(video, LANGUAGE):
    print(LANGUAGE, 'VIDEO DURATION:', video.duration)
    music = AudioFileClip(f'./assets/music1.wav').fx(volumex, factor=1.2).set_start(2.95).set_duration(video.duration-2.95)
    final_audio = CompositeAudioClip([video.audio, music]).set_fps(music.fps)
    #final_audio = audio_normalize(final_audio)
    video = video.set_audio(final_audio)
    video = crop(video, x1=656, width=608)
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    video.write_videofile(filename=f"./output/{date_str}[{LANGUAGE}].mp4", fps=24) #, audio_codec="aac", threads=12)#, logger=None)
LANGUAGE="Punjabi"
#for LANGUAGE in languages.keys():
if True:
    images = ["/home/siddharth/ShortGPT/resources/011WJF.jpg", "/home/siddharth/ShortGPT/resources/103308600.jpg", "/home/siddharth/ShortGPT/resources/103361347.jpg", "/home/siddharth/ShortGPT/resources/delhi-teachers-184315-16x9.png"]
    sentences = ["The President of India, Shreemati Droupadi Murmu, awarded National Awards to teachers from across the country on Teachers' Day.","In her speech, the President emphasized the importance of elementary education and the three-H formula for balanced development.", "She also highlighted the need for more female teachers to receive awards and the role of teachers in building the nation's future.", "The President stressed the duty of teachers and parents to recognize and develop the unique abilities of each child."]

    clips = createAssets(images, sentences, LANGUAGE)
    render = threading.Thread(target=renderVideo, args=(clips, LANGUAGE))
    render.start()
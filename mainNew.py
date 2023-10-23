import os
from sys import platform
if platform == "linux":
    os.environ['FFMPEG_BINARY'] = '/usr/bin/ffmpeg'
    os.environ['IMAGEMAGICK_BINARY'] = '/usr/bin/convert'
elif platform == "win32":
    pass

languages = { #0:code, 1:voice, 2:font, 3:fontsize 4:charlimit 5:fullstop 6:rate 7:gender
    "English": ("en", "HINDI", "./assets/fonts/English.ttf", 50, 125,'.','+15%',['female']), 
    "Hindi": ("hi", "HINDI", "./assets/fonts/Hindi.ttf", 50,125,u'।','+15%',['male','female']),
    "Marathi": ("mr", "MARATHI", "./assets/fonts/Hindi.ttf",50,125,'.','+15%',['male','female']),
    "Bengali": ("bn", "BENGALI", "./assets/fonts/Bengali.ttf",50,125,u'।','+15%',['male','female']),
    "Gujarati": ("gu", "GUJARATI", "./assets/fonts/Gujarati.ttf",50,125,'.','+15%',['male','female']),
    "Kannada": ("kn", "KANNADA", "./assets/fonts/Kannada.ttf",45,115,'.','+15%',['male','female']),
    "Malayalam": ("ml", "MALAYALAM", "./assets/fonts/Malayalam.ttf",45,85,'.','+15%',['male','female']),
    "Tamil": ("ta", "TAMIL", "./assets/fonts/Tamil.ttf",45,80,'.','+15%',['male','female']),
    "Telugu": ("te", "TELUGU", "./assets/fonts/Telugu.ttf",45,80,'.','+15%',['male','female']),
    "Urdu": ("ur", "URDU", "./assets/fonts/Urdu.ttf",45,105,u'۔','+15%',['male','female']),
}
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip, CompositeAudioClip, VideoFileClip
from moviepy.video.fx.all import crop, speedx
from moviepy.audio.fx.all import volumex, audio_normalize
from audio.voices import VOICENAMES, headers
from audio.tts import generate_voice, strip_silence, parse_webvtt, get_timed_images, adjust_timing
import ffmpeg
from gtts import gTTS
from visual.animations import Zoom, blur
from visual.images import getImagesfromQueries
from visual.transitions import slide_in, slide_out, crossfadein, crossfadeout
from visual.PIL_captions import TextImage
from visual.llm import image_queries, make_script, get_keywords
from googletrans import Translator
from easygoogletranslate import EasyGoogleTranslate
import subprocess, random, time, datetime
from pydub import AudioSegment
import threading
from PIL import Image, ImageFilter
import numpy as np
import gradio as gr

# def video_server(x):
#     time.sleep(4)
#     return x

# gr.Interface(video_server, "textbox", "textbox").queue().launch(share=True)


#translator = Translator()
resolution = (608, 1080)

def createAssets(images, script, LANGUAGE, header):
    while True:
        try:
            if LANGUAGE != "English":

                translator = EasyGoogleTranslate(
                    source_language='en',
                    target_language=languages[LANGUAGE][0],
                    timeout=10
                )
                script=translator.translate(script)
                #translations = translator.translate(script, src='en', dest=languages[LANGUAGE][0]) 
                #script = translations.text
                #pronounce = [translation.pronunciation for translation in translations]
            break
        except Exception as e:
            print(e, "Error in translation. Retrying...")
            time.sleep(5)

    toggle_slide = True

    # VoiceClip
    narrator_voice = random.choice(languages[LANGUAGE][7])
    while True:
        try:
            generate_voice(script, f'./tmp_assets/output{LANGUAGE}.wav', VOICENAMES[languages[LANGUAGE][1]][narrator_voice], rate=languages[LANGUAGE][6], LANGUAGE=LANGUAGE, words_in_cue=1)
            audio_clip = AudioFileClip(f'./tmp_assets/output{LANGUAGE}.wav')
            break
        except Exception as e:
            print(e, "Error in voice generation. Retrying...")
            time.sleep(5)
    
    
    clip_duration = audio_clip.duration

    # Base Image
    base = ImageClip('./assets/background.png').set_duration(clip_duration)

    # ImageClip
    image_clips = []
    blurred_images = []
    images = adjust_timing(images, images[-1][0][1], clip_duration)
    for image in images:

        image_clip = Zoom(image[1], image[0][1]-image[0][0], resolution, mode=random.choice(['in','out']), speed=(random.randint(20, 40)/10), fps=24)
        
        #blurred_image = ImageClip(image[1]).resize(height=resolution[1]).set_position(('center', 'center')).fl_image( blur )

        try:
            blurred_image = Image.open(image[1]).filter(ImageFilter.BoxBlur(5))
        except:
            blurred_image = Image.open(image[1]).convert('RGB').filter(ImageFilter.BoxBlur(5))
        blurred_image = ImageClip(np.array(blurred_image)).resize(height=resolution[1]).set_position(('center', 'center'))

        transitions_time = 0.5
        if toggle_slide:
            toggle_slide = False
            slide_direction = random.choice(['left','right'])
            image_clip = image_clip.set_start(image[0][0]).set_end(image[0][1])
            image_clip = slide_out(image_clip, transitions_time, slide_direction, resolution)
            image_clip = crossfadein(image_clip, 0.5)

            blurred_image = blurred_image.set_start(image[0][0]).set_end(image[0][1])
            blurred_image = crossfadeout(blurred_image, transitions_time)
        else:
            toggle_slide = True
            slide_direction = 'left' if slide_direction == 'right' else 'right'
            image_clip = image_clip.set_start(image[0][0]-transitions_time).set_end(image[0][1])
            image_clip = slide_in(image_clip, transitions_time, slide_direction, resolution)
            image_clip = crossfadeout(image_clip, transitions_time)

            blurred_image = blurred_image.set_start(image[0][0]-transitions_time).set_end(image[0][1])
            blurred_image = crossfadein(blurred_image, transitions_time)
        
        image_clips.append(image_clip)
        blurred_images.append(blurred_image)
        

    # TextClip
    captions = parse_webvtt(f'./tmp_assets/captions{LANGUAGE}.vtt', script, full_stop=languages[LANGUAGE][5])
    #.resize(height=text_clip.size[1])

    text_clips = []
    longest_text_clip=0
    onscreen_caption=[]
    onscreen_timing=[]
    start=0
    x=0
    for caption in captions:
        fontsize = languages[LANGUAGE][3]
        #TYPING EFFECT
        # if len(onscreen_caption)>languages[LANGUAGE][4]:
        #     onscreen_caption = ""
        #     start = caption[0][0]
        # onscreen_caption += caption[1]+' '

        # text_clip = (ImageClip(TextImage(onscreen_caption, font_path=languages[LANGUAGE][2], width=resolution[0]-15, fontsize=fontsize, color='#fbd504'))
        #             .set_start(start).set_end(caption[0][1]).set_position(('center', 610)))
        # text_clips.append(text_clip)
        # start=caption[0][1]

        #SCROLLING FROM BOTTOM EFFECT
        # if onscreen_caption=="": pass
        #     start = caption[0][0]
            
        onscreen_caption.append(caption[1])
        onscreen_timing.append(caption)
        if len(' '.join(onscreen_caption))>languages[LANGUAGE][4] or x==len(captions)-1:
            i=0
            #print(onscreen_timing)
            for highlight in onscreen_timing:
                #print(highlight[0][1], highlight[1])
                text_clip = (ImageClip(TextImage(onscreen_caption, highlight[1], i, font_path=languages[LANGUAGE][2], width=resolution[0]-15, 
                                                 fontsize=fontsize, color='#f9f9f9', highlight_color='#fbd504'))
                            .set_start(start).set_end(highlight[0][1]).set_position(('center', 610)))
                start = highlight[0][1]
                text_clips.append(text_clip)
                i+=1
            if text_clip.size[1]>longest_text_clip:
                longest_text_clip=text_clip.size[1]
            
            onscreen_caption = []
            onscreen_timing = []
            #text_clip = slide_in(text_clip, 0.3, 'bottom', resolution)
            #text_clip = crossfadeout(text_clip, 0.3)
        x+=1
            
    text_background = ImageClip('./assets/text_background.png').set_opacity(0.4).set_duration(clip_duration).set_position(('center', resolution[1]-(resolution[1]-700+60)-35))
    text_background = crop(text_background, y2=longest_text_clip+15)

    if header in headers.keys():
        header=headers[header]
    else:
        header = './assets/headers/header.png'
    header = ImageClip(header).set_duration(clip_duration).resize(width=resolution[0]-10).set_position(('center', 'top'))

    intro = VideoFileClip('./assets/intro.mp4').set_duration(2.95).set_start(0).set_position(('center', 'center')).crossfadeout(0.5)
    
    final_clip = CompositeVideoClip([base] + blurred_images + image_clips + [header, text_background] + text_clips).set_audio(audio_clip).set_start(2.95)
    final_clip = CompositeVideoClip([final_clip, intro])
    
    return final_clip

def renderVideo(video, LANGUAGE):
    #video = concatenate_videoclips(clips, method="chain")
    print(LANGUAGE, 'VIDEO DURATION:', video.duration)
    music = AudioFileClip(f'./assets/music1.wav').fx(volumex, factor=1.2).set_start(2.95).set_duration(video.duration-2.95)
    final_audio = CompositeAudioClip([video.audio, music]).set_fps(music.fps)
    #final_audio = audio_normalize(final_audio)
    video = video.set_audio(final_audio)
    video = crop(video, x1=656, width=608)
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    video.write_videofile(filename=f"./output/{date_str}[{LANGUAGE}].mp4", fps=24) #, audio_codec="aac", threads=12)#, logger=None)
            

startTime=time.time()
#script = "The President of India, Shrimati Droupadi Murmu, awarded National Awards to teachers from across the country on Teachers' Day. In her speech, the President emphasized the importance of elementary education and the three-H formula for balanced development." #She also highlighted the need for more female teachers to receive awards and the role of teachers in building the nation's future. The President stressed the duty of teachers and parents to recognize and develop the unique abilities of each child."
#script = "The Vice-President of India praised the successful G20 Leaders' Summit in New Delhi, stating that the outcomes will reshape the global order. He highlighted India's elevated stature on the global stage and the inclusive nature of its presidency. The Vice-President emphasized India's role in bridging divides and promoting peace. He mentioned initiatives such as the India-Middle East-Europe Economic Corridor and the Global Biofuels Alliance. The Vice-President also noted the inclusion of the African Union as a permanent member of the G20. He commended the shift towards a human-centric approach in the G20, focusing on sustainable development, digital infrastructure, green development, and women-led development. He encouraged participation in the upcoming Parliament-20 forum with the theme of unity and a shared future."
#script = "The President of India, Shrimati Droupadi Murmu, inaugurated the first Uttar Pradesh International Trade Show at Greater Noida. The event aims to showcase the products of Uttar Pradesh to both domestic and international markets. Over 2000 manufacturers and 400 buyers from 66 countries are participating in the trade show. The President emphasized the need to increase women's participation in entrepreneurship and labor force. She praised Uttar Pradesh's economic growth and investment initiatives, stating that the state is among the fastest-growing in the country. The President also highlighted the state's growing exports and expressed confidence in India becoming the third largest economy in the world."\
script = "Prime Minister Narendra Modi will launch nine new Vande Bharat Express trains on September 24th. These trains will improve connectivity across eleven states and will connect important religious sites such as Puri, Madurai, and Tirupati. The trains will be the fastest on their routes, saving passengers considerable time. The aim is to boost tourism and provide a world-class experience to passengers. The trains will have advanced safety features and amenities, including Kavach technology. This launch is in line with the Prime Minister's vision of improving connectivity and providing top-notch facilities to rail passengers."
#script = "In a historic move, the Chairman of Rajya Sabha, Jagdeep Dhankhar, has constituted an all-women panel of Vice-Chairpersons comprising 13 women Members. This decision was made as the Rajya Sabha discusses the Nari Shakti Vandan Vidheyak Bill, 2023. The presence of these women on the chair sends a powerful message and symbolizes their commanding position during this moment of change. The nominated women Members include prominent figures such as P.T. Usha, Jaya Bachchan, and Saroj Pandey. This move is a significant step towards promoting gender equality and empowering women in the political sphere."
sentences = script.split('. ')
keywords = get_keywords(script)
queries = image_queries(sentences)
images = getImagesfromQueries(queries, keywords=f'{""} 2023 India')
images = get_timed_images(sentences, images, languages['English'][6], languages['English'][7])
images = [((0, 4.682), './tmp_images/Prime Minister Narendra Modi will launch nine new Vande Bharat Express trains on September 24th/000001.jpg'), ((4.682, 11.222000000000001), './tmp_images/These trains will improve connectivity across eleven states and will connect important religious sites such as Puri, Madurai, and Tirupati/000001.jpg'), ((11.222000000000001, 14.962000000000002), './tmp_images/The trains will be the fastest on their routes, saving passengers considerable time/000001.jpg'), ((14.962000000000002, 18.53), './tmp_images/The aim is to provide a world-class experience to passengers and boost tourism/000001.jpg'), ((18.53, 22.332), './tmp_images/The trains will have advanced safety features and amenities, including Kavach technology/000001.jpg'), ((22.332, 28.224), "./tmp_images/This launch is in line with the Prime Minister's vision of improving connectivity and providing top-notch facilities to rail passengers./000005.jpg")]
print(images)
LANGUAGE = "English"
header = "Prime Minister's Office"
#for LANGUAGE in languages.keys():
if True:
    clips = createAssets(images, script, LANGUAGE, header)
    render = threading.Thread(target=renderVideo, args=(clips, LANGUAGE))
    render.start()
    # if LANGUAGE == "English":
    #     render.join()

render.join()
endTime=time.time()-startTime
print("Time taken:",endTime)

#/home/siddharth/Flipkart/venv/bin/python3 -m llama_cpp.server --model /home/siddharth/SIHShorts/models/llama-2-13b-chat.ggmlv3.q5_1.bin --n_gpu_layers 20 --use_mlock True
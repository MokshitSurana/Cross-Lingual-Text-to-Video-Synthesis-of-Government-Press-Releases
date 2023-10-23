import edge_tts
import asyncio
import os
import webvtt
import ffmpeg
from concurrent.futures import ThreadPoolExecutor
from audio.voices import VOICENAMES
import subprocess
from pydub import AudioSegment
from pydub.silence import detect_leading_silence

def run_async_func(loop, func):
    return loop.run_until_complete(func)
def generate_voice(text, outputfile, voice, rate, LANGUAGE="", words_in_cue=1):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            with ThreadPoolExecutor() as executor:
                loop.run_in_executor(executor, run_async_func, loop, async_generate_voice(text, outputfile, voice, rate, LANGUAGE=LANGUAGE, words_in_cue=words_in_cue))

        finally:
            loop.close()
        if not os.path.exists(outputfile):
            print("An error happened during edge_tts audio generation, no output audio generated")
            raise Exception("An error happened during edge_tts audio generation, no output audio generated")
        return outputfile

async def async_generate_voice(text, outputfile, voice, rate, LANGUAGE="", words_in_cue=1):
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate,)
            submaker = edge_tts.SubMaker()
            with open(outputfile, "wb") as file:
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        file.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
            if words_in_cue > 0:
                with open(f'./tmp_assets/captions{LANGUAGE}.vtt', "w", encoding="utf-8") as file:
                    file.write(submaker.generate_subs(words_in_cue=words_in_cue))
        except Exception as e:
            print("Error generating audio using edge_tts", e)
            raise Exception("An error happened during edge_tts audio generation, no output audio generated", e)
        return outputfile

def strip_silence(sound):
    trim_leading_silence = lambda x: x[detect_leading_silence(x) :]
    return trim_leading_silence(trim_leading_silence(sound.reverse()).reverse())

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return round(int(h) * 3600 + int(m) * 60 + float(s),3)

def add_full_stops(inputstr, arr, full_stop='.'):
    # Split the input string into sentences
    sentences = inputstr.split(full_stop)
    
    # Initialize an empty list to store the modified array
    modified_arr = []
    
    # Iterate over the array
    for i in range(len(arr)):
        # If the word ends a sentence, add a full stop
        if (i < len(arr) - 1 and any(sentence.strip().endswith(arr[i][1]) for sentence in sentences) and any(sentence.strip().startswith(arr[i+1][1]) for sentence in sentences)):
            modified_arr.append((arr[i][0],arr[i][1] + full_stop))
        else:
            modified_arr.append((arr[i][0],arr[i][1]))
    modified_arr[-1] = (modified_arr[-1][0],modified_arr[-1][1] + full_stop)
    
    sentences = inputstr.split(',')
    arr = modified_arr
    modified_arr = []
    for i in range(len(arr)):
        if (i < len(arr) - 1 and any(sentence.strip().endswith(arr[i][1]) for sentence in sentences) and any(sentence.strip().startswith(arr[i+1][1]) for sentence in sentences)):
            modified_arr.append((arr[i][0],arr[i][1] + ','))
        else:
            modified_arr.append((arr[i][0],arr[i][1]))
    return modified_arr


def parse_webvtt(file_path, script, full_stop='.'):
    captions = []
    for caption in webvtt.read(file_path):
        start_time = get_sec(caption.start)
        end_time = get_sec(caption.end)
        text = caption.text.strip()
        captions.append(((start_time, end_time), text))
    captions=add_full_stops(script, captions, full_stop)
    return captions
    

def get_timed_images(sentences, images, rate, narrator):
    output = []
    LANGUAGE="English"
    previous = 0
    i=0
    for i in range(len(sentences)):
        generate_voice(sentences[i], f'./tmp_assets/captions{LANGUAGE}.wav', VOICENAMES["ENGLISH"][narrator[-1]], rate, LANGUAGE, words_in_cue=1)
        #subprocess.call(['ffmpeg', '-i', f'./tmp_assets/captions{LANGUAGE}.wav', f'./tmp_assets/captionsffmpeg{LANGUAGE}.wav'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        ffmpeg.input(f'./tmp_assets/captions{LANGUAGE}.wav').output(f'./tmp_assets/captionsffmpeg{LANGUAGE}.wav').run(quiet=True)
        audio = strip_silence(AudioSegment.from_wav(f'./tmp_assets/captionsffmpeg{LANGUAGE}.wav')) + AudioSegment.silent(duration=250)
        output.append(((previous,(len(audio) / 1000.0)+previous), images[i]))
        previous += (len(audio) / 1000.0)
        os.remove(f'./tmp_assets/captionsffmpeg{LANGUAGE}.wav')
    return output

def adjust_timing(timed_image_urls, init_length, new_length):
    ratio = init_length/new_length
    new_timed_image_urls=[]
    for ele in timed_image_urls:
        start = round(ele[0][0]/ratio,2)
        end = round(ele[0][1]/ratio,2)
        new_timed_image_urls.append(((start,end),ele[1]))
    return new_timed_image_urls
import os
import subprocess

import yt_dlp
from shortGPT.config.languages import Language

from shortGPT.audio.audio_duration import get_asset_duration

import random

CONST_CHARS_PER_SEC = 20.5  # Arrived to this result after whispering a ton of shorts and calculating the average number of characters per second of speech.

WHISPER_MODEL = None


def downloadYoutubeAudio(url, outputFile):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "no_color": True,
        "no_call_home": True,
        "no_check_certificate": True,
        "format": "bestaudio/best",
        "outtmpl": outputFile
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            dictMeta = ydl.extract_info(
                url,
                download=True)
            if (not os.path.exists(outputFile)):
                raise Exception("Audio Download Failed")
            return outputFile, dictMeta['duration']
    except Exception as e:
        print("Failed downloading audio from the following video/url", e.args[0])
    return None


def speedUpAudio(tempAudioPath, outputFile, expected_duration=None):  # Speeding up the audio to make it under 60secs, otherwise the output video is not considered as a short.
    tempAudioPath, duration = get_asset_duration(tempAudioPath, False)
    if not expected_duration:
        if (duration > 57):
            subprocess.run(['ffmpeg', '-i', tempAudioPath, '-af', f'atempo={(duration/57):.5f}', outputFile])
        else:
            subprocess.run(['ffmpeg', '-i', tempAudioPath, outputFile])
    else:
        subprocess.run(['ffmpeg', '-i', tempAudioPath, '-af', f'atempo={(duration/expected_duration):.5f}', outputFile])
    if (os.path.exists(outputFile)):
        return outputFile


def ChunkForAudio(alltext, chunk_size=2500):
    alltext_list = alltext.split('.')
    chunks = []
    curr_chunk = ''
    for text in alltext_list:
        if len(curr_chunk) + len(text) <= chunk_size:
            curr_chunk += text + '.'
        else:
            chunks.append(curr_chunk)
            curr_chunk = text + '.'
    if curr_chunk:
        chunks.append(curr_chunk)
    return chunks


def audioToText(filename, language: Language = Language.ENGLISH, script=None, model_size="base.en"):
    code = "en"
    if language == Language.GUJARATI: 
        model_size="vasista22/whisper-gujarati-base"
        code = "gu"
    elif language == Language.TAMIL:
        model_size="vasista22/whisper-tamil-small"
        code = "ta"
    elif language == Language.KANNADA:
        model_size="vasista22/whisper-kannada-base"
        code = "kn"
    elif language == Language.TELUGU:
        model_size="vasista22/whisper-telugu-base"
        code = "te"
    elif language == Language.HINDI:
        model_size="vasista22/whisper-hindi-small"
        code = "hi"
    elif language == Language.BENGALI:
        model_size="sadidul012/whisper-small-bengali"
        code = "bn"
    elif language == Language.MARATHI:
        model_size="vittai23/whisper-small-marathiV3"
        code = "mr"
    elif language == Language.MALAYALAM:
        model_size="kavaymanohar/whisper-small-malayalam"
        code = "ml"
    elif language == Language.URDU:
        model_size="Abdullah17/whisper-small-urdu"
        code = "ur"
    from whisper_timestamped import load_model, transcribe_timestamped
    # global WHISPER_MODEL
    # if (WHISPER_MODEL == None):
    WHISPER_MODEL = load_model(model_size, device="cuda")
    gen = transcribe_timestamped(WHISPER_MODEL, filename, verbose=False, fp16=True,
                                 language=code, 
                                 seed=random.random(), 
                                 vad=True, 
                                 trust_whisper_timestamps=False,
                                 temperature = 0.0,
                                 initial_prompt=script,
                                 beam_size=20,
                                 patience=5,
                                )
    return gen


def getWordsPerSec(filename):
    a = audioToText(filename)
    return len(a['text'].split()) / a['segments'][-1]['end']


def getCharactersPerSec(filename):
    a = audioToText(filename)
    return len(a['text']) / a['segments'][-1]['end']

def run_background_audio_split(sound_file_path):
    try:
        # Run spleeter command
        # Get absolute path of sound file 
        output_dir = os.path.dirname(sound_file_path)
        command = f"spleeter separate -p spleeter:2stems -o '{output_dir}' '{sound_file_path}'"

        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # If spleeter runs successfully, return the path to the background music file
        if process.returncode == 0:
            return os.path.join(output_dir, sound_file_path.split("/")[-1].split(".")[0], "accompaniment.wav")
        else:
            return None
    except Exception:
        # If spleeter crashes, return None
        return None

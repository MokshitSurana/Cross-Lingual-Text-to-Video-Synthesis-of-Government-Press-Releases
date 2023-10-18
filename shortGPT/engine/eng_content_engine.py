import datetime
import os
import re
import shutil

from shortGPT.api_utils.pexels_api import getBestVideo
from shortGPT.audio import audio_utils
from shortGPT.audio.audio_duration import get_asset_duration
from shortGPT.audio.voice_module import VoiceModule
from shortGPT.config.asset_db import AssetDatabase
from shortGPT.config.languages import Language
from shortGPT.editing_framework.editing_engine import (EditingEngine,
                                                       EditingStep)
from shortGPT.editing_utils.handle_videos import extract_random_clip_from_video
from shortGPT.editing_utils import captions, editing_images
from shortGPT.engine.abstract_content_engine import AbstractContentEngine
from shortGPT.gpt import gpt_editing, gpt_translate, gpt_yt


class ContentVideoEngine(AbstractContentEngine):

    # def __init__(self, voiceModule: VoiceModule, script: str, background_music_name="", id="",
    #              watermark=None, isVerticalFormat=False, language: Language = Language.ENGLISH):
    #     super().__init__(id, "general_video", language, voiceModule)
    #     if not id:
    #         if (watermark):
    #             self._db_watermark = watermark
    #         if background_music_name:
    #             self._db_background_music_name = background_music_name
    #         self._db_script = script
    #         self._db_format_vertical = isVerticalFormat
    def __init__(self, script: str, keywords:str, short_type: str, voiceModule: VoiceModule, background_video_name="Minecraft jumping circuit", background_music_name="Music joakim karud dreams", short_id="",
                 num_images=None, watermark=None, language: Language = Language.ENGLISH, timed_image_urls=None, video_length=None, background_trimmed=None, 
                 timed_captions=None, listImageAssets=False, wordCount=30):
        super().__init__(short_id, short_type, language, voiceModule)
        if not short_id:
            if (num_images):
                self._db_num_images = num_images
            if (watermark):
                self._db_watermark = watermark
            self._db_background_video_name = background_video_name
            self._db_background_music_name = background_music_name
            self._db_script = script
            self._db_keywords = keywords
            self._db_timed_image_urls = timed_image_urls
            self._db_background_trimmed = None
            self._db_video_length = video_length
            self._db_timed_captions = timed_captions
            self.language = language
            self.listImageAssets = listImageAssets
            self.wordCount=wordCount

        self.stepDict = {
            1:  self._generateTempAudio,
            2:  self._speedUpAudio,
            3:  self._timeCaptions,
            4:  self._generateImageSearchTerms,
            5:  self._generateImageUrls,
            6:  self._chooseBackgroundMusic,
            7:  self._chooseBackgroundVideo,
            8:  self._prepareBackgroundAssets,
            9: self._prepareCustomAssets,
            10: self._editAndRenderShort,
            11: self._addMetadata
        }

    def _generateTempAudio(self):
        if not self._db_script:
            raise NotImplementedError("generateScript method must set self._db_script.")
        if (self._db_temp_audio_path):
            return
        self.verifyParameters(text=self._db_script)
        script = self._db_script
        # if (self._db_language != Language.ENGLISH.value):
        #     self._db_translated_script = gpt_translate.translateContent(script, self._db_language)
        #     script = self._db_translated_script
        self._db_temp_audio_path = self.voiceModule.generate_voice(
            script, self.dynamicAssetDir + "temp_audio_path.wav")

    def _speedUpAudio(self):
        if (self._db_audio_path):
            return
        self.verifyParameters(tempAudioPath=self._db_temp_audio_path)
        # Since the video is not supposed to be a short( less than 60sec), there is no reason to speed it up
        self._db_audio_path = self._db_temp_audio_path
        return
        self._db_audio_path = audio_utils.speedUpAudio(
            self._db_temp_audio_path, self.dynamicAssetDir+"audio_voice.wav")

    def _timeCaptions(self):
        if not self._db_timed_captions:
            self.verifyParameters(audioPath=self._db_audio_path)
            whisper_analysis = audio_utils.audioToText(self._db_audio_path, language=self.language, script=self._db_script)
            print(self.language=="ENGLISH")
            self._db_timed_captions = captions.getCaptionsWithTime(
                whisper_analysis, maxCaptionSize=self.wordCount, considerPunctuation=True)
            if self.language==Language.ENGLISH:
                self._db_timed_captions = captions.replaceWithScript(self._db_script, self._db_timed_captions)
            if not self._db_video_length: self._db_video_length = self._db_timed_captions[-1][0][1]
            print("CAPTIONS:",self._db_timed_captions)
            print("VIDEO LENGTH:",self._db_video_length)
            #if self.language!=Language.ENGLISH: input("GOOD RESULTS?")
        

    def _generateImageSearchTerms(self):
        if not self._db_timed_image_urls:
            self.verifyParameters(captionsTimed=self._db_timed_captions)
            if self._db_num_images:
                self._db_timed_image_searches = gpt_editing.getImageQueryPairs(
                    self._db_timed_captions, n=self._db_num_images)
            

    def _generateImageUrls(self):
        if not self._db_timed_image_urls:
            if self._db_timed_image_searches:
                self._db_timed_image_urls = editing_images.getImageUrlsTimed(
                    self._db_timed_image_searches, self._db_keywords, self.listImageAssets)
                
                #if input("GOOD RESULTS?")=='n':raise("BAD RESULTS")
        if self._db_video_length: 
            self._db_timed_image_urls = captions.adjust_timing(self._db_timed_image_urls, self._db_video_length, self._db_timed_captions[-1][0][1])

    def _chooseBackgroundMusic(self):
        if self._db_background_music_name:
            self._db_background_music_url = AssetDatabase.get_asset_link(self._db_background_music_name)

    def _chooseBackgroundVideo(self):
        self._db_background_video_url = AssetDatabase.get_asset_link(
            self._db_background_video_name)
        self._db_background_video_duration = AssetDatabase.get_asset_duration(
            self._db_background_video_name)

    def _prepareBackgroundAssets(self):
        self.verifyParameters(
            voiceover_audio_url=self._db_audio_path,
            video_duration=self._db_background_video_duration,
            background_video_url=self._db_background_video_url, music_url=self._db_background_music_url)
        if not self._db_voiceover_duration:
            self.logger("Rendering short: (1/4) preparing voice asset...")
            self._db_audio_path, self._db_voiceover_duration = get_asset_duration(
                self._db_audio_path, isVideo=False)
        if not self._db_background_trimmed:
            self.logger("Rendering short: (2/4) preparing background video asset...")
            self._db_background_trimmed = extract_random_clip_from_video(
                self._db_background_video_url, self._db_background_video_duration, self._db_voiceover_duration, self.dynamicAssetDir + "clipped_background.mp4")

    def _prepareCustomAssets(self):
        self.logger("Rendering short: (3/4) preparing custom assets...")
        pass

    def _editAndRenderShort(self):
        self.verifyParameters(
            voiceover_audio_url=self._db_audio_path,
            video_duration=self._db_background_video_duration,
            music_url=self._db_background_music_url)

        outputPath = self.dynamicAssetDir+"rendered_video.mp4"
        if not (os.path.exists(outputPath)):
            self.logger("Rendering short: Starting automated editing...")
            videoEditor = EditingEngine()
            videoEditor.addEditingStep(EditingStep.ADD_VOICEOVER_AUDIO, {
                                       'url': self._db_audio_path})
            videoEditor.addEditingStep(EditingStep.ADD_BACKGROUND_MUSIC, {'url': self._db_background_music_url,
                                                                          'loop_background_music': self._db_voiceover_duration,
                                                                          "volume_percentage": 0.70})
            videoEditor.addEditingStep(EditingStep.CROP_1920x1080, {
                                       'url': self._db_background_trimmed})
            #videoEditor.addEditingStep(EditingStep.ADD_SUBSCRIBE_ANIMATION, {'url': AssetDatabase.get_asset_link('subscribe animation')})

            # if self._db_watermark:
            #     videoEditor.addEditingStep(EditingStep.ADD_WATERMARK, {
            #                                'text': self._db_watermark})

            if self._db_num_images:
                for timing, image_url in self._db_timed_image_urls:
                    videoEditor.addEditingStep(EditingStep.SHOW_IMAGE, {'url': image_url,
                                                                        'set_time_start': timing[0],
                                                                        'set_time_end': timing[1]})
            caption_type = EditingStep.ADD_CAPTION_SHORT
            for timing, text in self._db_timed_captions:
                videoEditor.addEditingStep(caption_type, {'text': text,
                                                          'set_time_start': timing[0],
                                                          'set_time_end': timing[1]})
            

            videoEditor.renderVideo(outputPath, logger= self.logger if self.logger is not self.default_logger else None)

        self._db_video_path = outputPath

    def _addMetadata(self):
        if not os.path.exists('videos/'):
            os.makedirs('videos')
        #self._db_yt_title, self._db_yt_description = gpt_yt.generate_title_description_dict(self._db_script)
        self._db_yt_title = "Title"
        self._db_yt_description = "Description"
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        newFileName = f"videos/{date_str}[{self.language}]-" + \
            re.sub(r"[^a-zA-Z0-9 '\n\.]", '', self._db_yt_title)

        shutil.move(self._db_video_path, newFileName+".mp4")
        with open(newFileName+".txt", "w", encoding="utf-8") as f:
            f.write(
                f"---Youtube title---\n{self._db_yt_title}\n---Youtube description---\n{self._db_yt_description}")
        self._db_video_path = newFileName+".mp4"
        self._db_ready_to_upload = True

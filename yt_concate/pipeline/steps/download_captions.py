import time
from pytube import YouTube

from .step import Step
from yt_concate.tools.yt_logging import YtLogging
from yt_concate.multi_handler.yt_multi_threading import YtMultiThreading
from yt_concate.multi_handler.yt_multi_processing import YtMultiProcessing


class DownloadCaptions(Step):
    def __init__(self):
        self.download_caption_logging = YtLogging('download_captions')
        self.download_caption_logging.set_write_logging()

    def process(self, utils, inputs, data):
        start_time = time.time()
        # single handler
        # self.download_captions(data)
        # multi-threading
        # yt_multi_threading = YtMultiThreading()
        # yt_multi_threading.run_threading(self.download_captions_multi_handler, data, inputs)
        # multi-processing
        yt_multi_processing = YtMultiProcessing()
        yt_multi_processing.run_processing(self.download_captions_multi_handler, data, inputs)
        end_time = time.time()
        self.download_caption_logging.logger.debug('download captions cost time:%d', end_time - start_time)
        return data

    def download_captions(self, data):
        for yt in data:
            if yt.check_caption_file_exists():
                self.download_caption_logging.logger.debug('%s.txt file exists!!!', yt.caption_id)
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except Exception as e:
                continue

            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

    def download_captions_multi_handler(self, *args, **kwargs):
        for yt in args:
            if yt.check_caption_file_exists():
                self.download_caption_logging.logger.debug('%s.txt file exists!!!', yt.caption_id)
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except Exception as e:
                continue

            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

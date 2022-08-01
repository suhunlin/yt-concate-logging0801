import time
from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS
from yt_concate.multi_handler.yt_multi_processing import YtMultiProcessing
from yt_concate.multi_handler.yt_multi_threading import YtMultiThreading
from yt_concate.tools.yt_logging import YtLogging


class DownloadVideos(Step):
    def __str__(self):
        return '<class DownloadVideo: This class is use for download all video form Found data structure>' + '\n'

    def __init__(self):
        self.download_video_logging = YtLogging('download_video')
        self.download_video_logging.set_write_logging()

    def process(self, utils, inputs, data):
        yt_set = set([found.yt for found in data])
        yt_list = list(yt_set)
        self.download_video_logging.logger.debug('before:%d, after:%d', len(data), len(yt_set))
        start_time = time.time()
        t1 = YtMultiProcessing()
        t1.run_processing(self.download_videos_by_multi_handler, yt_list, inputs)
        end_time = time.time()
        self.download_video_logging.logger.debug('download time:%d', end_time - start_time)
        return data

    def download_videos(self, yt_set):
        for yt in yt_set:
            if yt.check_video_file_exists():
                print(yt.caption_id + '.mp4 file exists!')
                continue
            # print('Downloading...', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS, filename=yt.caption_id + '.mp4')

    def download_videos_by_multi_handler(self, *args, **kwargs):
        for yt in args:
            if yt.check_video_file_exists():
                self.download_video_logging.logger.debug('%s.mp4 file exists!!!', yt.caption_id)
                continue
            # print('Downloading...', yt.url)
            self.download_video_logging.logger.debug('Downloading...%s', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS, filename=yt.caption_id + '.mp4')

    def __str__(self):
        return '<class DownloadVideo: This class is use for download all video form Found data structure>' + '\n'

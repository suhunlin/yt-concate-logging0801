import os

from yt_concate.tools.yt_logging import YtLogging

from yt_concate.settings import OUTPUTS
from yt_concate.settings import DOWNLOADS
from yt_concate.settings import VIDEOS
from yt_concate.settings import CAPTIONS


class Utils:
    def __init__(self):
        self.utils_logging = YtLogging('yt_command')
        self.utils_logging.set_write_logging()

    def create_dir(self):
        os.makedirs(OUTPUTS, exist_ok=True)
        os.makedirs(DOWNLOADS, exist_ok=True)
        os.makedirs(VIDEOS, exist_ok=True)
        os.makedirs(CAPTIONS, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        self.utils_logging.logger.debug('video_list_filepath:%s', os.path.join(DOWNLOADS, channel_id + '.txt'))
        return os.path.join(DOWNLOADS, channel_id + '.txt')

    def check_video_list_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_output_filepath(self, filename):
        return os.path.join(OUTPUTS, filename + '.mp4')

import os
import sys

CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
config_path = CURRENT_DIR.rsplit('/', 1)[0]
sys.path.append(config_path)

from tools.utils import Utils
from tools.yt_logging import YtLogging
from tools.yt_command_line import YtCommandLine
from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.initialize_yt import InitializeYt
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.edit_video import EditVideo

def main():
    main_logging = YtLogging('main')
    main_logging.set_write_logging()
    main_logging.logger.debug('----start main----')
    utils = Utils()
    yt_command_line = YtCommandLine(utils)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),

    ]
    inputs = {
        'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA',
        'search_word': 'incredible',
        'limit': 20,
    }
    inputs.update(yt_command_line.run_command_line())
    main_logging.logger.debug('inputs:%s', inputs)
    p1 = Pipeline(steps)
    p1.run_pipeline(utils, inputs)


if __name__ == '__main__':
    main()

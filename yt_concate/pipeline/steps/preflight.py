from .step import Step
from yt_concate.tools.yt_logging import YtLogging


class Preflight(Step):
    def __init__(self):
        preflight_logging = YtLogging('preflight')
        preflight_logging.set_write_logging()

    def process(self, utils, inputs, data):
        utils.create_dir()
        return 'create dri success!!!'

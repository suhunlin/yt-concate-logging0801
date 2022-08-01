from .step import Step
from yt_concate.models.yt import Yt
from yt_concate.tools.yt_logging import YtLogging


class InitializeYt(Step):
    def __init__(self):
        self.initialize_yt_logging = YtLogging('initialize_yt')
        self.initialize_yt_logging.set_write_logging()

    def process(self, utils, inputs, data):
        self.initialize_yt_logging.logger.debug('%s', [Yt(url) for url in data])
        return [Yt(url) for url in data]

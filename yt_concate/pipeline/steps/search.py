from .step import Step
from yt_concate.tools.yt_logging import YtLogging
from yt_concate.models.found import Found

class Search(Step):
    def __init__(self):
        self.search_logging = YtLogging('search')
        self.search_logging.set_write_logging()

    def process(self, utils, inputs, data):
        found = []
        search_word = inputs['search_word']
        for yt in data:
            if not yt.check_caption_file_exists():
                self.search_logging.logger.debug('%s .txt file not exists!!', yt.caption_id)
                continue
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        for obj in found:
            self.search_logging.logger.debug('%s, %s, %s', obj.yt, obj.caption, obj.time)
        return found

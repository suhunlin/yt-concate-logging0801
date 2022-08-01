from .step import Step
from yt_concate.tools.yt_logging import YtLogging


class ReadCaptions(Step):
    def __init__(self):
        self.read_captions_logging = YtLogging('read_captions')
        self.read_captions_logging.set_write_logging()

    def process(self, utils, inputs, data):
        self.read_captions(data)
        # for yt in data:
        #     self.read_captions_logging.logger.debug('captions:%s', yt.captions)
        return data

    def read_captions(self, data):
        for yt in data:
            if not yt.check_caption_file_exists():
                self.read_captions_logging.logger.debug('%s .txt not exists!!!', yt.caption_id)
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
                yt.captions = captions

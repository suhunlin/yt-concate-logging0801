from yt_concate.tools.yt_logging import YtLogging

class Pipeline:
    def __init__(self, steps):
        self.steps = steps
        self.pipeline_logging = YtLogging('pipeline')
        self.pipeline_logging.set_write_logging()

    def run_pipeline(self, utils, inputs):
        data = None
        for step in self.steps:
            data = step.process(utils, inputs, data)
        self.pipeline_logging.logger.debug('step:%s, data:%s', step, data)
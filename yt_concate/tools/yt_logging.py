import os
import logging

from yt_concate.settings import LOGS


class YtLogging:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        self.filepath = self.get_logging_filepath(logger_name)
        self.logger_formatter = logging.Formatter('%(levelname)s:%(funcName)s:%(asctime)s:%(message)s')
        self.logger.setLevel(logging.DEBUG)
        self.make_logs_dir()

    def make_logs_dir(self):
        os.makedirs(LOGS, exist_ok=True)

    def set_write_logging(self):
        file_handler = logging.FileHandler(self.filepath)
        file_handler.setFormatter(self.logger_formatter)
        file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)

    def get_logging_filepath(self, filename):
        return os.path.join(LOGS, filename + '.log')

import os
from threading import Thread

from yt_concate.tools.yt_logging import YtLogging


class YtMultiThreading:
    def __init__(self):
        self.yt_multi_threading_logging = YtLogging('yt_multi_threading')
        self.yt_multi_threading_logging.set_write_logging()

    def run_threading(self, target, iterable_data, inputs_dict):
        threads = []
        equal_part_tuple = tuple(self.equal_parts_data(iterable_data))
        self.yt_multi_threading_logging.logger.debug('multi_threading_handle_data:%s', equal_part_tuple)

        for core in range(os.cpu_count()):
            threads.append(Thread(target=target, args=equal_part_tuple[core], kwargs=inputs_dict))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def equal_parts_data(self, iterable_data):
        divide_num = int(len(iterable_data) / os.cpu_count())
        if len(iterable_data) % os.cpu_count() != 0:
            divide_num += 1
        equal_parts_list = [iterable_data[i:i + divide_num] for i in range(0, len(iterable_data), divide_num)]
        return equal_parts_list

import sys
import getopt

from .yt_logging import YtLogging


class YtCommandLine:
    def __init__(self, utils):
        self.short_opt = 'hc:s:l:'
        self.long_opt = 'channel_id= search_word= limit='.split()
        self.yt_commaind_logging = YtLogging('yt_command')
        self.yt_commaind_logging.set_write_logging()

    def print_useage(self):
        self.yt_commaind_logging.logger.info('python3 yt_concate project OPTIONS')
        self.yt_commaind_logging.logger.info('OPTIONS:')
        self.yt_commaind_logging.logger.info(
            '{:>6} {:<16}{}'.format('-c', '--channel_id', 'Channel id is the Youtube Channel to Download'))
        self.yt_commaind_logging.logger.info(
            '{:>6} {:<16}{}'.format('-s', '--search_word', 'Search the key word from Download Captions'))
        self.yt_commaind_logging.logger.info(
            '{:>6} {:<16}{}'.format('-l', '--limit', 'Video number to edit form Download Video'))
        self.yt_commaind_logging.logger.info('{}'.format('    main.py -c <channel_id> -s <search_word>'))

    def run_command_line(self):
        key = None
        value = None
        inputs = {}
        try:
            opts, args = getopt.getopt(sys.argv[1:], self.short_opt, self.long_opt)
        except getopt.GetoptError:
            print('command_lind_opt.py -h <inputfile> -o <outputfile>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                self.print_useage()
            elif opt in ('-c', '--channel_id'):
                key = 'channel_id'
                value = arg
            elif opt in ('-s', '--search_word'):
                key = 'search_word'
                value = arg
            elif opt in ('-l', '--limit'):
                key = 'limit'
                value = arg

            inputs[key] = value
        if not inputs:
            self.yt_commaind_logging.logger.debug('command_line:%s')
        else:
            self.yt_commaind_logging.logger.debug('command_line:%s', inputs)
        return inputs

import urllib.request
import json

from .step import Step
from yt_concate.settings import API_KEY
from yt_concate.tools.yt_logging import YtLogging


class GetVideoList(Step):
    def __init__(self):
        self.get_video_list_logging = YtLogging('get_video_list')
        self.get_video_list_logging.set_write_logging()

    def process(self, utils, inputs, data):
        return self.get_all_video_in_channel(utils, inputs)

    def get_all_video_in_channel(self, utils, inputs):
        api_key = API_KEY
        channel_id = inputs['channel_id']
        filepath = utils.get_video_list_filepath(channel_id)
        if utils.check_video_list_exists(filepath):
            self.get_video_list_logging.logger.debug('%s.txt file exists!!!', channel_id)
            return self.read_video_links(filepath)

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        self.write_video_links(filepath, video_links)
        return video_links

    def write_video_links(self, filepath, video_links):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_video_links(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for line in f:
                video_links.append(line.strip())
        return video_links

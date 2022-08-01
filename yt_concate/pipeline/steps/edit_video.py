from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step
from yt_concate.tools.yt_logging import YtLogging


class EditVideo(Step):
    def __init__(self):
        self.edit_video_logging = YtLogging('edit_video')
        self.edit_video_logging.set_write_logging()

    def process(self, utils, inputs, data):
        clips = []
        for found in data:
            if not found.yt.captions:
                self.edit_video_logging.logger.debug('Captions is none!!!')
                continue
            if found.yt.caption_id == 'b9dWgUlMb9o':
                continue

            start, end = self.parse_caption_time(found.time)
            # print(start, end)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= int(inputs['limit']):
                break
        final_clip = concatenate_videoclips(clips)
        filename = inputs['channel_id'] + '_' + inputs['search_word']
        final_clip.write_videofile(utils.get_output_filepath(filename))

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time):
        h, m, s = time.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000

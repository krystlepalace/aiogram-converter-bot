import subprocess
from config import CONFIG


class AudioConverter:
    def __init__(self, path, song_name):
        self.input_path = path
        self.output_path = f"{CONFIG.media_full_path}{song_name.split('.')[0]}." + "{}"

    async def convert_audio(self, output_format):
        self.output_path = self.output_path.format(output_format)
        subprocess.run(
            [CONFIG.ffmpeg_path, "-i", self.input_path, "-vn", "-ar", "44100",
             "-ac",
             "2", "-b:a", "192k", self.output_path])

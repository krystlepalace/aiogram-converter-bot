import subprocess
from config import CONFIG


class VideoConverter:
    def __init__(self, path):
        self.input_path = path
        self.output_path = f"{path.split('.')[0]}" + ".{}"

    async def convert_video(self, output_format):
        self.output_path = self.output_path.format(output_format)
        if output_format == "gif":
            subprocess.run(
                [CONFIG.ffmpeg_path, "-i", self.input_path,
                 "-r", "15",
                 "-filter_complex", "fps=60,scale=320:-1",
                 self.output_path])
        elif output_format == "mp3":
            subprocess.run(
                [CONFIG.ffmpeg_path, "-i", self.input_path,
                 "-b:a", "192k",
                 "-vn",
                 self.output_path])
        elif output_format == "webm":
            subprocess.run(
                [CONFIG.ffmpeg_path, "-i", self.input_path,
                 "-vcodec", "libvpx",
                 "-acodec", "libvorbis",
                 self.output_path])
        else:
            subprocess.run(
                [CONFIG.ffmpeg_path, "-i", self.input_path,
                 self.output_path])

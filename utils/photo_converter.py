from PIL import Image


class PhotoConverter:
    def __init__(self, path: str):
        self.input_path = path
        self.output_path = ""
        self.image = image = Image.open(path)

    async def convert_photo(self, output_format):
        self.output_path = f"{self.input_path.split('.')[0]}.{output_format}"
        self.image.save(self.output_path)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.callbacks.converter_callback import FormatCallback


MEDIA_FORMATS = {
  "AUDIO": ['MP3', 'WAV', 'OGG',
            'FLAC', 'M4A', 'AAC',
            'AMR', 'OPUS', 'AIFF'],
  "PHOTO": ['PNG', 'JPG', 'JPEG',
            'BMP', 'GIF', 'WEBP',
            'SVG', 'ICO', 'TIFF'],
  "VIDEO": ["MP4", "MP3", "GIF",
            "AVI", "MOV", "WEBM",
            "M4A", "MPEG", "WMV"]
}

def formats_keyboard_builder(format_name):
  builder = InlineKeyboardBuilder()
  for format in FORMATS[format_name]:
      builder.button(text=format, callback_data=FormatCallback(
          format=format.lower(), type=format_name
      ).pack())
  builder.adjust(3)

  return builder

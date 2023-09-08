from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.callbacks.converter_callback import FormatCallback

audio_formats = ['MP3', 'WAV', 'OGG',
                 'FLAC', 'M4A', 'AAC',
                 'AMR', 'OPUS', 'AIFF']
photo_formats = ['PNG', 'JPG', 'JPEG',
                 'BMP', 'GIF', 'WEBP',
                 'SVG', 'ICO', 'HDR']


def audio_formats_builder():
    builder = InlineKeyboardBuilder()
    for format in audio_formats:
        builder.button(text=format, callback_data=FormatCallback(
            format=format.lower(), type='AUDIO'
        ).pack())
    builder.adjust(3)

    return builder


def photo_formats_builder():
    builder = InlineKeyboardBuilder()
    for format in photo_formats:
        builder.button(text=format, callback_data=FormatCallback(
            format=format.lower(), type='PHOTO'
        ).pack())
    builder.adjust(3)

    return builder

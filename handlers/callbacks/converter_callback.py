from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.filters.callback_data import CallbackData
from utils.photo_converter import PhotoConverter
from pathlib import Path
from config import CONFIG
import main
import os


router = Router()


class FormatCallback(CallbackData, prefix="convert"):
    type: str
    format: str


@router.callback_query(
    FormatCallback.filter(F.type.in_(['PHOTO']))
)
async def process_image_convert(callback: CallbackQuery,
                                callback_data: FormatCallback):
    await callback.message.edit_text(text="Working...")

    file_id = callback.message.reply_to_message.photo[-1].file_id
    file = await main.bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path(f"{CONFIG.media_full_path}{file_id}.{file_path.split('.')[-1]}")
    await main.bot.download_file(file_path, destination=file_on_disk)

    # convertation
    converter = PhotoConverter(file_on_disk.__str__())
    await converter.convert_photo(callback_data.format)

    await main.bot.send_document(chat_id=callback.from_user.id,
                                 document=FSInputFile(converter.output_path))

    await callback.answer()
    os.remove(file_on_disk)

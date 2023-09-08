from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.photo)
async def convert_photo(message: Message):
    await message.reply("Formats: ")

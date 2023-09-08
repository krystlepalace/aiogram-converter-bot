from aiogram import Router, F
from aiogram.types import Message
from keyboards.choose_formats import photo_formats_builder


router = Router()


@router.message(F.photo)
async def convert_photo(message: Message):
    await message.reply("Formats: ",
                        reply_markup=photo_formats_builder().as_markup())

from aiogram import Router, F
from aiogram.types import Message
from keyboards.choose_formats import formats_keyboard_builder


router = Router()


@router.message(F.photo)
async def convert_photo(message: Message):
    await message.reply("Formats: ",
                        reply_markup=formats_keyboard_builder(format_name="PHOTO").as_markup())


@router.message(F.audio or F.voice)
async def convert_audio(message: Message):
    await message.reply("Formats: ",
                        reply_markup=formats_keyboard_builder(format_name="AUDIO").as_markup())


@router.message(F.video)
async def convert_video(message: Message):
    await message.reply("Formats: ",
                        reply_markup=formats_keyboard_builder(format_name="VIDEO").as_markup())

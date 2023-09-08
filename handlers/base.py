from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("This bot can convert media files to different "
                         "formats. Just send file to bot and choose your "
                         "format.\n"
                         "For any help use /help")


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("If you want to convert some media file - just send "
                         "itm you will see inline menu with different formats "
                         "pop up. Just click on what you want and wait for "
                         "results!")

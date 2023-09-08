import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, media_handler
from handlers.callbacks import converter_callback
from utils.commands import set_commands


bot = Bot(token=CONFIG.bot_token.get_secret_value())


async def main():
    dp = Dispatcher()

    dp.include_routers(base.router,
                       media_handler.router,
                       converter_callback.router
                       )

    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

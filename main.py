import asyncio

from config import config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from tg_bot.handlers.system import system_router


async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(system_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

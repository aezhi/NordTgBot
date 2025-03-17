# добавить nonchat middleware чтобы работала админ панель только в личном чате
# посмотреть на этом ютуб канале видео как защитить бота от ддос
# log.py в utils
# фиксануть log.py чтобы все логировало
# pep8 minor changes
#запустить код в мейне обернутый в трай эксепт и сделать ошибку в функции где будет трай эксепт

import asyncio

from config import config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from tg_bot.log import logger
from tg_bot.handlers import *
from tg_bot.middlewares import *


async def main():
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode='HTML'),
    )

    dp = Dispatcher()

    dp.update.outer_middleware(BlockPrivateMessagesMiddleware())
    dp.update.outer_middleware(LoggingMiddleware())
    dp.message.middleware(ThrottlingMiddleware())

    dp.include_router(system_router)
    dp.include_router(admin_router)
    dp.include_router(user_router)

    try:
        await dp.start_polling(bot, skip_updates=True)

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    asyncio.run(main())

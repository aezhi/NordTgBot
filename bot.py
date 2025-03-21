import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from bot.handlers import *
from bot.middlewares import *

from bot.config import config
from bot.utils.log import logger


async def main():
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode='HTML'),
    )
    dp = Dispatcher()

    dp.update.outer_middleware(BlockPrivateMessagesMiddleware())
    dp.update.outer_middleware(LoggingMiddleware())
    dp.message.middleware(ThrottlingMiddleware())

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot, skip_updates=True)

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    asyncio.run(main())

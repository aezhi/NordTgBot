import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import config
from tg_bot.handlers.system import system_router
from tg_bot.handlers.user import user_router
from tg_bot.middlewares.antispam import AntiFloodMiddleware

async def main():
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode='HTML')
    )
    dp = Dispatcher()

    # Register our AntiFloodMiddleware
    dp.message.middleware(AntiFloodMiddleware(threshold=1.0, mute_duration=10.0))

    # Add routers
    dp.include_router(system_router)
    dp.include_router(user_router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import BaseMiddleware

from tg_bot.log import log_chat_activity


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        log_chat_activity(event)
        return await handler(event, data)

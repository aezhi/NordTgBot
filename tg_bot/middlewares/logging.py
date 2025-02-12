from aiogram import BaseMiddleware

from log import log_chat_activity, log_exception


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            log_chat_activity(event)
            return await handler(event, data)
        except Exception as e:
            log_exception(str(e))

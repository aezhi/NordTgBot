from aiogram import BaseMiddleware

from bot.filters.admin import IsAdmin


class BlockPrivateMessagesMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        message = event.message or event.edited_message

        if message and message.chat.type == 'private':
            if not await IsAdmin().__call__(message):
                return

        return await handler(event, data)

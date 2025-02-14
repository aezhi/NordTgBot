from aiogram import BaseMiddleware


class BlockPrivateMessagesMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.message and event.message.chat.type == 'private':
            return

        if event.edited_message and event.edited_message.chat.type == 'private':
            return

        return await handler(event, data)

import time
import asyncio

from aiogram import BaseMiddleware
from aiogram.types import Message, ChatMemberAdministrator, ChatMemberOwner

from tg_bot.utils.moderation import mute_user


class AntiFloodMiddleware(BaseMiddleware):
    """
    Check if a user sent a message in a group/supergroup quicker than `threshold` seconds
    after their previous message. If so, mute them for `mute_duration`.
    """

    def __init__(self, message_cooldown: int = 1, mute_duration: int = 30):
        super().__init__()
        self.message_cooldown = message_cooldown
        self.mute_duration = mute_duration
        self.last_message_time = {} # (chat_id: int, user_id: int) : current_time: time.time()

    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            if event.chat.type in ('group', 'supergroup'):
                chat_id = event.chat.id
                user_id = event.from_user.id
                bot = data['bot']

                if isinstance(await bot.get_chat_member(chat_id, user_id), (ChatMemberAdministrator, ChatMemberOwner)):
                    return await handler(event, data)

                current_time = time.time()
                last_time = self.last_message_time.get((chat_id, user_id), 0)

                if current_time - last_time < self.message_cooldown:
                    await mute_user(bot, chat_id, user_id, self.mute_duration)
                    warning_message = await event.reply('Ты отправляешь сообщения слишком часто!')

                    await asyncio.sleep(10)
                    await bot.delete_message(chat_id, warning_message.message_id)

                else:
                    self.last_message_time[(chat_id, user_id)] = current_time

        return await handler(event, data)

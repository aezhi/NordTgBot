from aiogram.filters import BaseFilter
from aiogram.types import Message, chat_member

from bot.config import config


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type == 'private':
            return str(message.from_user.id) in config.ADMIN_IDS.split(',')

        member: chat_member.ChatMember = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in ('administrator', 'creator')

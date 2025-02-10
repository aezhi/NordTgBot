from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.exceptions import TelegramBadRequest


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
            return member.status in ("administrator", "creator")
        except TelegramBadRequest:
            return False

from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsNotGroupMessage(BaseFilter):
    async def __call__(self, event: Union[Message, CallbackQuery]) -> bool:
        if isinstance(event, Message):
            return event.chat.type not in ('group', 'supergroup')

        return event.message.chat.type not in ('group', 'supergroup')

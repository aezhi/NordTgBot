from aiogram import Router, F
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

system_router = Router()


@system_router.message(F.new_chat_members)
async def remove_join_message(message: Message):
    try:
        await message.delete()
    except TelegramBadRequest:
        pass


@system_router.message(F.left_chat_member)
async def remove_left_message(message: Message):
    try:
        await message.delete()
    except TelegramBadRequest:
        pass

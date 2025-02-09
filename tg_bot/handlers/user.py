from aiogram import Router, F
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

user_router = Router()


@user_router.message()
async def echo_handler(message: Message) -> None:
    await message.answer(f"Echo: {message.text}")

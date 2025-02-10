from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from tg_bot.filters.admin import IsAdmin

admin_router = Router()


@admin_router.message(Command("mute"), IsAdmin())
async def mute_command(message: Message):
    await message.answer("You are an admin, so you can use this command.")

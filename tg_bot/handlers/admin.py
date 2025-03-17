from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from tg_bot.filters.admin import IsAdmin
from tg_bot.keyboards.admin import build_admin_keyboard

admin_router = Router()


@admin_router.message(CommandStart, IsAdmin())
async def show_admin_panel(message: Message):
    await message.answer('Админ панель', reply_markup=build_admin_keyboard())


@admin_router.callback_query(F.da)
async def send_log_file(call: CallbackQuery):
    print(1)

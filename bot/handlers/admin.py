import os

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile

from bot.utils.log import logger
from bot.keyboards.admin import *
from bot.filters import IsAdmin, IsNotGroupMessage

admin_router = Router()


@admin_router.message(Command('start'), IsAdmin(), IsNotGroupMessage())
async def show_admin_panel(message: Message):
    await message.answer('Админ панель', reply_markup=main_keyboard)


@admin_router.callback_query(F.data == 'log', IsNotGroupMessage())
async def send_log_file(callback: CallbackQuery):
    try:
        log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'logs', 'chat_activity.log')

        if not os.path.exists(log_file_path):
            await callback.answer('Файл не найден', show_alert=True)
            return

        await callback.message.reply_document(document=FSInputFile(log_file_path))
        await callback.answer()

    except Exception as e:
        logger.error(e)

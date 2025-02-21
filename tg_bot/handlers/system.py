from aiogram import Router, F
from aiogram.types import Message

from loguru import logger

system_router = Router()


@system_router.message(F.new_chat_members)
async def remove_join_message(message: Message):
    try:
        await message.delete()

    except Exception as e:
        logger.error(e)


@system_router.message(F.left_chat_member)
async def remove_left_message(message: Message):
    try:
        await message.delete()

    except Exception as e:
        logger.error(e)

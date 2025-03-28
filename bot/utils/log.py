import os
import sys

from loguru import logger

from bot.config import config

from typing import Union
from aiogram.types import Update, CallbackQuery

os.makedirs('../../logs', exist_ok=True)

logger.remove()
logger.add(
    sink='logs/chat_activity.log',
    format='[+] {message}',
    level='INFO',
    rotation=f'{config.LOG_ROTATION_SIZE} MB',
    compression='zip',
    encoding='utf-8',
)
logger.add(
    sink='logs/exceptions.log',
    format='[+] {time:MMM D, YYYY - HH:mm:ss} | {file} | line: {line} | {level} | {message}\n',
    level='ERROR',
    rotation=f'{config.LOG_ROTATION_SIZE} MB',
    compression='zip',
    encoding='utf-8',
)
logger.add(
    sink=sys.stdout,
    format='[+] {time:MMM D, YYYY - HH:mm:ss} | {file} | line: {line} | <level>{level}</level> | {message}\n',
    level='ERROR',
)


def log_chat_activity(event: Union[Update, str]) -> None:
    if isinstance(event, Update):
        if event.callback_query:
            callback: CallbackQuery = event.callback_query
            if callback.message:
                logger.info(
                    f'[Callback Query] | {callback.message.date} | From: {callback.from_user.full_name} (ID: {callback.from_user.id}) '
                    f'| Chat: {callback.message.chat.id} | Data: {callback.data}'
                )
            else:
                logger.info(
                    f'[Callback Query] | From: {callback.from_user.full_name} (ID: {callback.from_user.id}) | Data: {callback.data}'
                )

        elif event.message:
            message = event.message

            match True:
                case True if message.new_chat_members:
                    for user in message.new_chat_members:
                        logger.info(
                            f'[User Joined] | {message.date} | User: {user.full_name} (ID: {user.id}) '
                            f'joined chat {message.chat.title} (ID: {message.chat.id})'
                        )

                case True if message.left_chat_member:
                    user = message.left_chat_member
                    logger.info(
                        f'[User Left] | {message.date} | User: {user.full_name} (ID: {user.id}) '
                        f'left chat {message.chat.title} (ID: {message.chat.id})'
                    )

                case True if message.text:
                    logger.info(
                        f'[Message] | {message.date} | From: {message.from_user.full_name} '
                        f'(ID: {message.from_user.id}) | Chat: {message.chat.id} | Text: {message.text}'
                    )

                case True if message.animation:
                    logger.info(
                        f'[GIF] | {message.date} | From: {message.from_user.full_name} (ID: {message.from_user.id}) '
                        f'| Chat: {message.chat.id} | GIF file_id: {message.animation.file_id}'
                    )

                case True if message.photo:
                    logger.info(
                        f'[Photo] | {message.date} | From: {message.from_user.full_name} (ID: {message.from_user.id}) '
                        f'| Chat: {message.chat.id} | file_id: {message.photo[0].file_id}'
                    )

                case True if message.video:
                    logger.info(
                        f'[Video] | {message.date} | From: {message.from_user.full_name} (ID: {message.from_user.id}) '
                        f'| Chat: {message.chat.id} | Video file_id: {message.video.file_id}'
                    )

                case True if message.sticker:
                    logger.info(
                        f'[Sticker] | {message.date} | From: {message.from_user.full_name} (ID: {message.from_user.id}) '
                        f'| Chat: {message.chat.id} | Sticker emoji: {message.sticker.emoji}, file_id: {message.sticker.file_id}'
                    )

                case True if message.voice:
                    logger.info(
                        f'[Voice message] | {message.date} | From: {message.from_user.full_name} '
                        f'(ID: {message.from_user.id}) | Chat: {message.chat.id} | Voice file_id: {message.voice.file_id}'
                    )

                case True if message.audio:
                    logger.info(
                        f'[Audio] | {message.date} | From: {message.from_user.full_name} (ID: {message.from_user.id}) '
                        f'| Chat: {message.chat.id} | file_id: {message.audio.file_id}, title: {message.audio.title or "N/A"}'
                    )

                case _:
                    logger.info(
                        f'[Non-text Message] | {message.date} | From: {message.from_user.full_name} '
                        f'(ID: {message.from_user.id}) | Chat: {message.chat.id}'
                    )

        else:
            logger.info(event)

    else:
        logger.error(f'Unknown event! | {event}')

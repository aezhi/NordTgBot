import os
import sys

from loguru import logger
from aiogram.types import Update

os.makedirs('logs', exist_ok=True)

logger.remove()
logger.add(
    sink='logs/chat_activity.log',
    format='[+] {message}',
    level='INFO',
    rotation='10 MB',
    compression='zip',
    encoding='utf-8',
)
logger.add(
    sink='logs/exceptions.log',
    format='[+] {time:MMM D, YYYY - HH:mm:ss} | {file} | line: {line} | {level} | {message}\n',
    level='ERROR',
    rotation='10 MB',
    compression='zip',
    encoding='utf-8',
)
logger.add(
    sink=sys.stdout,
    format='[+] {time:MMM D, YYYY - HH:mm:ss} | {file} | line: {line} | <level>{level}</level> | {message}\n',
    level='ERROR',
)


def log_chat_activity(event: Update | str) -> None:
    if isinstance(event, Update):
        if event.message:
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
            logger.error(f'Not a message event! | {event}')

    elif isinstance(event, str):
        logger.info(event)

    else:
        logger.error(f'Uknown event! | {event}')

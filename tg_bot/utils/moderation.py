from datetime import datetime, timedelta, timezone
from log import logger, log_chat_activity

from aiogram.types import ChatPermissions


async def mute_user(bot, chat_id: int, user_id: int, mute_duration: int) -> None:
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,
    )

    try:
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            until_date=timedelta(seconds=mute_duration),
        )

        log_chat_activity(
            f'[User Muted] | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S+00:00')} '
            f'| User ID: {user_id} muted in chat ID: {chat_id} for {mute_duration} seconds'
        )

    except Exception as e:
        logger.critical(e)

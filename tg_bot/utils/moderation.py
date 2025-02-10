from datetime import timedelta

from aiogram.types import ChatPermissions
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError


async def mute_user(bot, chat_id: int, user_id: int, mute_duration: int) -> None:
    """

    """

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
        print(f"User {user_id} is muted for {mute_duration} seconds (until_date={30}).")
    except (TelegramBadRequest, TelegramForbiddenError) as e:
        print(f"[mute_user] Error while restricting user {user_id} in chat {chat_id}: {e}")

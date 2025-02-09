from datetime import timedelta
from aiogram.types import ChatPermissions
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

async def mute_user(bot, chat_id: int, user_id: int, mute_duration: float) -> None:
    """
    Temporarily restrict a user from sending messages (mute) for `mute_duration` seconds.
    Rely solely on Telegram's `until_date` to handle the unmute.
    """
    # Current timestamp


    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,  # or False, adjust to your group policy
    )

    try:
        # Telegram will automatically lift this restriction once `until_date` is reached
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            until_date=timedelta(seconds=30),
        )
        print(f"User {user_id} is muted for {mute_duration} seconds (until_date={30}).")
    except (TelegramBadRequest, TelegramForbiddenError) as e:
        print(f"[mute_user] Error while restricting user {user_id} in chat {chat_id}: {e}")

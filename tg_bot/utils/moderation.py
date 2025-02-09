import time
from aiogram.types import ChatPermissions
from aiogram.exceptions import TelegramBadRequest

async def mute_user(bot, chat_id: int, user_id: int, mute_duration: float) -> None:
    """
    Mute (restrict) a user from sending messages in a chat for a given duration.

    :param bot: Bot instance.
    :param chat_id: The chat ID where the user should be muted.
    :param user_id: The user ID to mute.
    :param mute_duration: Duration in seconds for which the user is muted.
    :return: True if muting was successful, False otherwise.
    """
    
    now = time.time()
    until_date = int(now + mute_duration)
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,  # You may adjust these as needed.
    )
    try:
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            until_date=until_date,
        )

    except TelegramBadRequest as e:
        print(f"Failed to mute user {user_id} in chat {chat_id}: {e}")


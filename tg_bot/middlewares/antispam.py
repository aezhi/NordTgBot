import time
from aiogram import BaseMiddleware
from aiogram.types import Message

from tg_bot.utils.moderation import mute_user


class AntiFloodMiddleware(BaseMiddleware):
    """
    This middleware checks if a user in a group/supergroup sent a message
    less than `threshold` seconds after their last message.
    If so, the user is muted for `mute_duration` seconds.
    """

    def __init__(self, threshold: float = 1.0, mute_duration: float = 10.0):
        super().__init__()
        self.threshold = threshold
        self.mute_duration = mute_duration
        # Dictionary to store the last message timestamp per (chat_id, user_id)
        self.last_message_time = {}

    async def __call__(self, handler, event, data):
        """
        Intercept incoming messages before they reach the handler.
        """
        if isinstance(event, Message):
            chat = event.chat
            user = event.from_user
            if chat and user and chat.type in ("group", "supergroup"):
                now = time.time()
                last_time = self.last_message_time.get((chat.id, user.id), 0)

                # Check if time delta < threshold
                if now - last_time < self.threshold:
                    # Attempt to mute the user
                    try:
                        bot = data["bot"]  # Bot instance is provided in data by Aiogram
                        await mute_user(
                            bot=bot,
                            chat_id=chat.id,
                            user_id=user.id,
                            mute_duration=self.mute_duration
                        )
                    except Exception as e:
                        print(f"[AntiFloodMiddleware] Error muting user {user.id}: {e}")

                # Update last message time
                self.last_message_time[(chat.id, user.id)] = now

        # Continue to the next handler in the chain
        return await handler(event, data)

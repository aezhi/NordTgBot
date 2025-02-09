import time
from aiogram import BaseMiddleware
from aiogram.types import Message

from tg_bot.utils.moderation import mute_user


class AntiFloodMiddleware(BaseMiddleware):
    """
    Check if a user sent a message in a group/supergroup quicker than `threshold` seconds
    after their previous message. If so, mute them for `mute_duration`.
    """

    def __init__(self, threshold: float = 1.0, mute_duration: int = 30):
        super().__init__()
        self.threshold = threshold
        self.mute_duration = mute_duration
        # Dictionary storing last message time per (chat_id, user_id)
        self.last_message_time = {}

    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            chat_id = event.chat.id
            user_id = event.from_user.id
            # Only act in group/supergroup
            if event.chat.type in ("group", "supergroup"):
                now = time.time()
                last_time = self.last_message_time.get((chat_id, user_id), 0)

                # If user is sending messages faster than `threshold`
                if now - last_time < self.threshold:
                    bot = data["bot"]  # Aiogram injects the bot instance into `data`
                    await mute_user(bot, chat_id, user_id, self.mute_duration)

                # Update the last message timestamp
                self.last_message_time[(chat_id, user_id)] = now

        return await handler(event, data)

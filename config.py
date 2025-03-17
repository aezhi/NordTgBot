from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass(frozen=True)
class Config:
    BOT_TOKEN: str = getenv('BOT_TOKEN')
    ADMIN_GROUP_ID: int = int(getenv('ADMIN_GROUP_ID'))
    LOG_ROTATION_SIZE: int = int(getenv('LOG_ROTATION_SIZE'))
    MESSAGE_RATE_LIMIT: int = int(getenv('MESSAGE_RATE_LIMIT'))
    BASIC_MUTE_DURATION: int = int(getenv('BASIC_MUTE_DURATION'))


config = Config()

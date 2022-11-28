from typing import Optional

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from bot.config import load_config


class IsAdmin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, message: Message) -> bool:
        try:
            admins = load_config().tg_bot.admin_ids
        except AttributeError:
            admins = []
        return message.from_user.id in admins

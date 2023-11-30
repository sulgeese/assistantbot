from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from typing import Dict, Any, Awaitable, Callable

from bot.settings import settings


class GroupMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if data['event_chat'].type == 'private' or \
           (data['event_chat'].type == 'supergroup' and data['event_chat'].id == settings.bots.supergroup_id):
            return await handler(event, data)

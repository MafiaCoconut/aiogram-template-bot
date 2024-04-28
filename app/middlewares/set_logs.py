from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject, Message, CallbackQuery
from aiogram.dispatcher.event.handler import HandlerObject
from db.postgresql_handlers.users_db_handler import user_is_exists
from icecream import ic

from utils.logs import set_func, set_func_and_person


class SetLogMiddleware(BaseMiddleware):
    """
    A class whose purpose is to check whether a user is registered in the database or not
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        if isinstance(event, Message):
            set_func_and_person(function=data['handler'].callback.__name__, message=event, status = 'debug')

        elif isinstance(event, CallbackQuery):
            set_func_and_person(function=data['handler'].callback.__name__, message=event.message, status='debug')

        return await handler(event, data)




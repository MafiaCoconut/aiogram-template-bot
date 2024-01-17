from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from models.sqlite.persons_sqlite import PersonSQLite


class SomeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # print("Before handler")
        try:
            user_id = data["event_from_user"].id
            person_sqlite = PersonSQLite()
            language = person_sqlite.get_language(user_id)

            data['language'] = language
        except Exception as e:
            data['language'] = 'en'

        result = await handler(event, data)

        # print("After handler")
        return result

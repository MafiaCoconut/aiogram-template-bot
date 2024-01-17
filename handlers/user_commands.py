import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from handlers import auxiliary
from keyboards import inline, reply, inline_admin

from models.sqlite.persons_sqlite import PersonSQLite
from config.log_def import set_func, set_func_and_person
from utils.fluent import list_of_available_languages
from utils.states import ChangeLanguageFromStart
from utils.bot import bot

router = Router()
tag = "user_commands"
status = "debug"


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    if not await state.get_data():
        chat_id = message.chat.id
        username = message.from_user.username
        person = PersonSQLite()

        language = message.from_user.language_code
        if language not in list_of_available_languages:
            language = 'en'

        l10n = auxiliary.get_l10n(language)

        if not person.is_exists(chat_id):
            person.save_person(chat_id=chat_id, username=username, language=language)
            logging.info(f"Добавлен пользователь: {username}/{chat_id}. Язык: {message.from_user.language_code}")
            await auxiliary.send_message_to_admin(f"Добавлен пользователь:\n\n"
                                                  f"id: {chat_id}\n"
                                                  f"username: @{username}\n"
                                                  f"language: {message.from_user.language_code}",
                                                  _reply_markup=inline_admin.get_person_by_id(chat_id))

            await message.answer(l10n.format_value('welcome-message'),
                                 reply_markup=inline.get_settings_language_from_start(l10n))
        else:
            await message.answer(l10n.format_value('reactivating-the-bot'), reply_markup=inline.get_main_menu(l10n))


@router.message(Command("main_menu"))
async def command_main_menu_handler(message: Message, state: FSMContext, language: str) -> None:
    function_name = "main_menu_handler"
    set_func_and_person(function_name, tag, message)

    l10n = auxiliary.get_l10n(language)
    if not await state.get_data():
        await message.answer(l10n.format_value('menu-main'),
                             reply_markup=inline.get_main_menu(l10n))


async def send_main_menu_from_mailing_handler(call: CallbackQuery, language: str) -> None:
    function_name = "send_main_menu_from_mailing_handler"
    set_func_and_person(function_name, tag, call.message, status)

    l10n = auxiliary.get_l10n(language)

    await call.message.answer(l10n.format_value('menu-main'),
                              reply_markup=inline.get_main_menu(l10n))
    await call.answer()

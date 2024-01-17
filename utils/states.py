from aiogram.fsm.state import StatesGroup, State


class GetPersonById(StatesGroup):
    last_help_message_id = State()


class DeletePersonById(StatesGroup):
    last_help_message_id = State()
    chat_id = State()

class ChangeMailingTime(StatesGroup):
    time = State()


class ChangeParserTime(StatesGroup):
    time = State()


class SendingMessageForEveryone(StatesGroup):
    message_id = State()
    text = State()
    time = State()
    buttons = State()
    replyz_markup = State()


class DeleteMailing(StatesGroup):
    message_id = State()
    id_job = State()


class ChangePersonsParameters(StatesGroup):
    message_id = State()
    chat_id = State()
    username = State()
    parameters = State()
    show_time = State()
    change_time = State()
    change_numbers = State()


class SendFeedback(StatesGroup):
    message_id = State()
    text = State()
    check = State()


class ChangeLanguageFromStart(StatesGroup):
    message_id = State()





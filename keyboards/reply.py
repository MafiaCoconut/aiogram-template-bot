from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

rkr = ReplyKeyboardRemove()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить меню на сегодня")],
        [KeyboardButton(text="Столовые")],
        [KeyboardButton(text="Ссылки")],
        [KeyboardButton(text="Инструкции")],
        [KeyboardButton(text="Настройки")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

settings = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"Ежедневная рассылка меню Mensa: ")],
        [KeyboardButton(text=f"Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,

)

admin_back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


def get_back(l10n):
    back = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=l10n.format_value('back'))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return back


admin_change_persons_parameters = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Показать время рассылки")],
        [KeyboardButton(text="Изменить время рассылки")],
        # [KeyboardButton(text="Изменить отображение цифр в меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


send_feedback = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да")],
        [KeyboardButton(text="Нет")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

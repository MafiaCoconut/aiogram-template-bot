from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

menu_help = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пользователи", callback_data="admin_menu_users")],
        [InlineKeyboardButton(text="Столовые", callback_data="admin_menu_canteens")],
        [InlineKeyboardButton(text="Stadburo", callback_data="admin_menu_stadburo")],
        [InlineKeyboardButton(text="Логи", callback_data="admin_menu_logs")],
        [InlineKeyboardButton(text="Рассылка", callback_data="admin_menu_mailing")],
    ]
)

menu_users = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Список пользователей", callback_data="admin_get_all_persons")],
        [InlineKeyboardButton(text="username, time, created", callback_data="admin_get_username_time_created")],
        [InlineKeyboardButton(text="id, username, time", callback_data="admin_get_id_username_time")],
        [InlineKeyboardButton(text="Изменить параметры", callback_data="admin_change_persons_parameters")],
        [InlineKeyboardButton(text="Получить ссылку на пользователя", callback_data="admin_get_person_by_id")],
        [InlineKeyboardButton(text="Удалить пользователя", callback_data="admin_delete_person")],

        [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],
    ]
)

menu_canteens = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Запуск парсера всех", callback_data="admin_start_canteen_parser_all")],

        [InlineKeyboardButton(text="Erlenring парсер", callback_data="admin_start_canteen_parser_mensa_erlenring"),
         InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_mensa_erlenring")],

        [InlineKeyboardButton(text="Lahnberge парсер", callback_data="admin_start_canteen_parser_mensa_lahnberge"),
         InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_mensa_lahnberge")],

        [InlineKeyboardButton(text="Bistro парсер", callback_data="admin_start_canteen_parser_bistro"),
         InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_bistro")],

        [InlineKeyboardButton(text="Cafeteria парсер", callback_data="admin_start_canteen_parser_cafeteria_lahnberge"),
         InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_cafeteria_lahnberge")],

        [InlineKeyboardButton(text="Mo diner парсер", callback_data="admin_start_canteen_parser_mo_diner"),
         InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_mo_diner")],

        [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

    ]
)

menu_stadburo = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Запустить парсер", callback_data="admin_start_termins_parser")],

        [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

    ]
)

menu_logs = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Прислать логи", callback_data="admin_send_logs")],
        [InlineKeyboardButton(text="Очистить логи", callback_data="admin_clear_logs")],

        [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

    ]
)

menu_mailing = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить сообщение всем", callback_data="admin_menu_send_msg4all")],
        [InlineKeyboardButton(text="Получить все рассылки", callback_data="admin_get_all_mailing")],
        [InlineKeyboardButton(text="Удалить рассылку", callback_data="admin_delete_mailing")],

        [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

    ]
)


def get_go_to(where):
    go_to = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад",
                                  callback_data=f"admin_menu_{where}"),
             InlineKeyboardButton(text="В главное меню",
                                  callback_data="admin_menu_help")]
        ]
    )
    return go_to


person_parameters = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Изменить время рассылки", callback_data="admin_change_person_mailing_time")],
        # [InlineKeyboardButton(text="Изменить отображение цифр в меню", callback_data="change_person_numbers_in_menu")],
    ]
)


def get_change_person_parameters(where):
    person_parameters_new = person_parameters
    back_keyboard = get_go_to(where)
    person_parameters_new.inline_keyboard.append(back_keyboard.inline_keyboard[0])
    # person_parameters_new.inline_keyboard.append(back_keyboard.inline_keyboard[1])
    return person_parameters_new


def get_msg4all_main():
    msg4all_main = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Изменить текст', callback_data='admin_msg4all_change_text')],
            [InlineKeyboardButton(text='Изменить время', callback_data='admin_msg4all_change_time')],
            [InlineKeyboardButton(text='Изменить кнопки', callback_data='admin_msg4all_change_buttons')],
            [InlineKeyboardButton(text='Готово', callback_data='admin_msg4all_ready_to_send')],

        ]
    )
    go_to = get_go_to('mailing')
    msg4all_main.inline_keyboard.append([*go_to.inline_keyboard[0]])
    return msg4all_main


def get_msg4all_ready_to_send():
    msg4all = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Отправить', callback_data='admin_msg4all_send')],
            [InlineKeyboardButton(text='Вернуться', callback_data='admin_menu_send_msg4all')],
            [InlineKeyboardButton(text='В главное меню', callback_data='admin_menu_help')],
        ]
    )

    return msg4all


# msg4all_check = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Далее", callback_data="admin_msg4all_next")],
#         [InlineKeyboardButton(text="Изменить", callback_data="admin_msg4all_change")],
#         [InlineKeyboardButton(text="Отменить", callback_data="admin_menu_mailing")],
#         [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],
#     ]
#
# )


def get_person_by_id(chat_id):
    person = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Перейти на акк человека", url=f'tg://user?id={chat_id}')]
        ]
    )
    go_to = get_go_to('users')
    person.inline_keyboard.append([*go_to.inline_keyboard[0]])
    return person


def get_delete_person():
    delete_person = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да", callback_data='admin_delete_person_yes')],
            [InlineKeyboardButton(text="Нет", callback_data='admin_delete_person_no')]
        ]
    )
    go_to = get_go_to('users')
    delete_person.inline_keyboard.append([*go_to.inline_keyboard[0]])
    return delete_person


change_text = InlineKeyboardButton(text="Изменить текст", callback_data="admin_msg4all_change_text")
add_time = InlineKeyboardButton(text="Добавить время", callback_data="admin_msg4all_add_time")
change_time = InlineKeyboardButton(text="Изменить время", callback_data="admin_msg4all_change_time")
add_button = InlineKeyboardButton(text="Добавить кнопку", callback_data="admin_msg4all_next") # вводить сначала текст кнопки, потом callbackdata
delete_button = InlineKeyboardButton(text="Удалить кнопку", callback_data="admin_msg4all_next")
change_button = InlineKeyboardButton(text="Изменить кнопку", callback_data="admin_msg4all_next")
InlineKeyboardButton(text="Отменить", callback_data="admin_menu_mailing")
InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")




"""
добавить время 
изменить время
добавить кнопку


Сообщение:
Тестовое сообщение

Время отправки:
-----------
Добавить время




"""
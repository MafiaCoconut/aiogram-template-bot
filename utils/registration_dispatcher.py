from aiogram import Dispatcher, F

# from handlers.callback import
# from handlers.admin.commands import logs, users, stadburo, canteens, mailing, users_processing
# from middlewares.languages import SomeMiddleware


dp = Dispatcher()
# dp.message.middleware(SomeMiddleware())
# dp.callback_query.outer_middleware(SomeMiddleware())


def include_routers():
    dp.include_routers(
        # main_menu_callback.router,
        # user_commands.router,
        # admin_commands.router,
        # bot_messages.router,


    )


def register_all_callbacks():
    # # Help меню админа
    # register_admin_help_menu()
    #
    # # Главное меню
    # dp.callback_query.register(main_menu_callback.menu_main_handler,
    #                            F.data == 'menu_main')
    #
    # # Столовые
    # dp.callback_query.register(canteens_callback.menu_canteens_handler, F.data == "menu_canteens")
    # dp.callback_query.register(canteens_callback.canteens_handler, F.data.startswith('canteen'))
    #
    # # Ссылки
    # dp.callback_query.register(links_callback.menu_links_handler, F.data == 'menu_links')
    # dp.callback_query.register(links_callback.show_others_links_handler, F.data == 'open_others_links')
    # dp.callback_query.register(links_callback.show_main_links_handler, F.data == 'show_main_links')
    #
    # # Термины
    # dp.callback_query.register(stadburo_menu_callback.menu_stadburo_handler, F.data == 'menu_stadburo')
    #
    # #       Эмиграционное меню
    # dp.callback_query.register(stadburo_immigration_callback.menu_immigration_handler, F.data == 'menu_immigration')
    # dp.callback_query.register(stadburo_immigration_callback.aufenthaltstitel_handler, F.data == 'aufenthaltstitel')
    # dp.callback_query.register(stadburo_immigration_callback.adressanderung_handler, F.data == 'adressanderung')
    # dp.callback_query.register(stadburo_immigration_callback.eat_abholung_handler, F.data == 'eat_abholung')
    #
    # dp.callback_query.register(stadburo_menu_callback.registration_handler, F.data == 'registration')
    # dp.callback_query.register(stadburo_menu_callback.stadtburo_others_handler, F.data == 'stadtburo_others')
    #
    # # Настройки
    # dp.callback_query.register(settings_callback.menu_settings_handler, F.data == "menu_settings")
    # dp.callback_query.register(settings_callback.change_mailing_time_handler, F.data == "change_mailing_time")
    # dp.callback_query.register(settings_callback.change_status_mailing_handler, F.data == 'change_status_mailing')
    # dp.callback_query.register(settings_callback.change_status_numbers_in_menu_handler,
    #                            F.data == 'change_status_numbers_in_menu')
    # dp.callback_query.register(settings_callback.change_language_handler, F.data.startswith('settings_language'))
    #
    # # Донаты
    # dp.callback_query.register(main_menu_callback.menu_donations_handler, F.data == "menu_donations")
    #
    # # Дополнительное меню
    # dp.callback_query.register(additionally_menu_callback.menu_additionally_handler, F.data == 'menu_additionally')
    # dp.callback_query.register(additionally_menu_callback.menu_manuals_handler, F.data == 'manuals')
    #
    # #       Обратная связь
    # dp.callback_query.register(feedback_callback.menu_feedback_handler, F.data == 'menu_feedback')
    # dp.callback_query.register(feedback_callback.show_contacts_handler, F.data == 'contacts')
    # dp.callback_query.register(feedback_callback.send_response_handler, F.data == 'response')
    #
    # # Feedback
    # dp.callback_query.register(feedback_callback.send_feedback_form_check, F.data.startswith('feedback'))
    #
    # # Админ
    # # dp.callback_query.register(admin_callback.show_person_mailing_time_handler,
    # #                            F.data == 'show_person_mailing_time')
    # # dp.callback_query.register(admin_callback.change_person_mailing_time_handler,
    # #                            F.data == 'change_person_mailing_time')
    # # dp.callback_query.register(admin_callback.change_person_numbers_in_menu_handler,
    # #                            F.data == 'change_person_numbers_in_menu')
    #
    # # Выводить меню после рассылки
    # dp.callback_query.register(user_commands.send_main_menu_from_mailing_handler, F.data == 'send_menu_main')


def register_admin_help_menu():
    # Пользователи
    # dp.callback_query.register(users.admin_menu_users, F.data == 'admin_menu_users')
    # dp.callback_query.register(users.admin_get_all_persons_handler, F.data == 'admin_get_all_persons')
    # dp.callback_query.register(users.admin_get_username_time_created_handler,
    #                            F.data == 'admin_get_username_time_created')
    # dp.callback_query.register(users.admin_get_id_username_time_handler, F.data == 'admin_get_id_username_time')
    # dp.callback_query.register(users.admin_change_persons_parameters_handler,
    #                            F.data == 'admin_change_persons_parameters')
    # dp.callback_query.register(users.admin_get_person_by_id_handler, F.data == 'admin_get_person_by_id')
    # dp.callback_query.register(users.admin_delete_person_handler, F.data == 'admin_delete_person')
    # dp.callback_query.register(users_processing.admin_delete_person_decision_handler,
    #                            F.data.startswith('admin_delete_person_'))
    # dp.callback_query.register(users.admin_change_persons_mailing_time_handler,
    #                            F.data == 'admin_change_person_mailing_time')
    #
    # # Столовые
    # dp.callback_query.register(canteens.admin_menu_canteens, F.data == 'admin_menu_canteens')
    # dp.callback_query.register(canteens.admin_start_canteens_parser, F.data.startswith('admin_start_canteen'))
    # dp.callback_query.register(canteens.admin_get_canteens_menu, F.data.startswith('admin_get_canteen'))
    #
    # # Stadburo
    # dp.callback_query.register(stadburo.admin_menu_stadburo, F.data == 'admin_menu_stadburo')
    # dp.callback_query.register(stadburo.admin_start_termins_parser_handler, F.data == 'admin_start_termins_parser')
    #
    # # логи
    # dp.callback_query.register(logs.admin_menu_logs, F.data == 'admin_menu_logs')
    # dp.callback_query.register(logs.admin_send_logs_handler, F.data == 'admin_send_logs')
    # dp.callback_query.register(logs.admin_clear_logs_handler, F.data == 'admin_clear_logs')
    #
    # # Рассылка
    # dp.callback_query.register(mailing.admin_menu_mailing, F.data == 'admin_menu_mailing')
    # dp.callback_query.register(mailing.admin_menu_send_msg4all, F.data == 'admin_menu_send_msg4all')
    # dp.callback_query.register(mailing.admin_get_all_mailing_handler, F.data == 'admin_get_all_mailing')
    # dp.callback_query.register(mailing.admin_delete_mailing_handler, F.data == 'admin_delete_mailing')
    #
    # # Отправка сообщения всем
    # dp.callback_query.register(mailing.admin_send_msg4all_change_text, F.data == 'admin_msg4all_change_text')
    # dp.callback_query.register(mailing.admin_send_msg4all_change_time, F.data == 'admin_msg4all_change_time')
    # dp.callback_query.register(mailing.admin_send_msg4all_ready_to_send, F.data == 'admin_msg4all_ready_to_send')
    # dp.callback_query.register(mailing.admin_send_msg4all_send, F.data == 'admin_msg4all_send')
    #
    # # Открыть главное меню
    # dp.callback_query.register(admin_commands.admin_menu_help_callback,
    #                            F.data == 'admin_menu_help', IsAdminCallback())
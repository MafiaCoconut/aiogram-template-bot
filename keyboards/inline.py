from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from fluent.runtime import FluentLocalization


def get_main_menu(l10n: FluentLocalization):
    main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('main-menu-canteen'), callback_data="menu_canteens")],
            [InlineKeyboardButton(text=l10n.format_value('main-menu-links'), callback_data="menu_links")],
            [InlineKeyboardButton(text=l10n.format_value('main-menu-stadburo'), callback_data="menu_stadburo")],
            [InlineKeyboardButton(text=l10n.format_value('main-menu-settings'), callback_data="menu_settings")],
            [InlineKeyboardButton(text=l10n.format_value('main-menu-donation'), callback_data="menu_donations")],
            [InlineKeyboardButton(text=l10n.format_value('main-menu-additionally'), callback_data="menu_additionally")],
        ]
    )
    return main_menu


def get_canteens(l10n):
    canteens = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Mensa Erlenring",
                                  callback_data="canteen_mensa_erlenring")],

            [InlineKeyboardButton(text="Mensa Lahnberge",
                                  callback_data="canteen_mensa_lahnberge")],

            [InlineKeyboardButton(text="Bistro",
                                  callback_data="canteen_bistro")],

            [InlineKeyboardButton(text="Cafeteria Lahnberge",
                                  callback_data="canteen_cafeteria_lahnberge"),

             InlineKeyboardButton(text="Mo's Diner",
                                  callback_data="canteen_mo_diner"),

             InlineKeyboardButton(text="Colibri",
                                  callback_data="canteen_colibri")],

            [InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return canteens


def get_main_links(l10n):
    main_links = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Marvin",
                                     url="https://marvin.uni-marburg.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces"),
                InlineKeyboardButton(text="Ilias",
                                     url="https://ilias.uni-marburg.de/login.php?cmd=force_login"),
                InlineKeyboardButton(text="Mail",
                                     url="https://home.students.uni-marburg.de/login.php"),
            ],
            [
                InlineKeyboardButton(text="Bibliothek",
                                     url="https://arbeitsplatz.ub.uni-marburg.de/index.php?location=gruppen"),
                InlineKeyboardButton(text="Rückzahlung",
                                     url="https://idp.hebis.de/ub-marburg/Authn/UserPassword"),

            ],
            [
                InlineKeyboardButton(text="Mensa",
                                     url="https://studierendenwerk-marburg.de/essen-trinken/speisekarte/")

            ],
            [
                InlineKeyboardButton(text="Stadburo",
                                     url="https://termine-reservieren.de/termine/marburg/")
            ],
            [
                InlineKeyboardButton(text=l10n.format_value('others-links'),
                                     callback_data="open_others_links"),

                InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                     callback_data="menu_main"),
            ],

        ]
    )
    return main_links


def get_others_links(l10n):
    others_links = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="VPN",
                                     url="https://www.uni-marburg.de/de/hrz/dienste/vpn"),
                InlineKeyboardButton(text="WiFi",
                                     url="https://www.uni-marburg.de/de/hrz/dienste/wlan"),
                InlineKeyboardButton(text="Printer",
                                     url="https://www.uni-marburg.de/de/hrz/dienste/kopieren-drucken-scannen"),
            ],
            [
                InlineKeyboardButton(text="Deutsche Ticket",
                                     url="https://weblogin.uni-marburg.de/idp/profile/SAML2/POST/SSO?execution=e1s2"),
                InlineKeyboardButton(text="Deutsche Radio",
                                     url="https://www.rundfunkbeitrag.de/meldedaten/"),

                # InlineKeyboardButton(text="Nextbike",
                #                      url=""),
            ],
            [
                InlineKeyboardButton(text=l10n.format_value('freebies'),
                                     url="https://medium.com/@alex.kach.2222/халява-c223847b7bcb"),
                # InlineKeyboardButton(text="Deutsche Ticket",
                #                      url="https://weblogin.uni-marburg.de/idp/profile/SAML2/POST/SSO?execution=e1s2"),

                # InlineKeyboardButton(text="Nextbike",
                #                      url=""),
            ],
            [
                InlineKeyboardButton(text=l10n.format_value('main-links'),
                                     callback_data="show_main_links"),

                InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                     callback_data="menu_main"),

            ]
        ]
    )
    return others_links


def get_stadburo(l10n):
    stadburo = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ausländerbehörde / Immigration Office",
                                  callback_data="menu_immigration")],

            [InlineKeyboardButton(text="Stadtbüro / Registration Office",
                                  callback_data="registration")],

            [InlineKeyboardButton(text="Others",
                                  callback_data="stadtburo_others")],

            [InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return stadburo


def get_immigration(l10n):
    immigration = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Aufenthaltstitel beantragen",
                                  callback_data="aufenthaltstitel")],
            [InlineKeyboardButton(text="Adressänderung",
                                  callback_data="adressanderung")],
            [InlineKeyboardButton(text="eAT-Abholung",
                                  callback_data="eat_abholung")],

            [InlineKeyboardButton(text=l10n.format_value('back'),
                                  callback_data="menu_stadburo"),
             InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return immigration


def get_manuals(l10n):
    manuals = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Token",
                                  url="https://medium.com/@alex.kach.2222/получение-токена-71123ce74556"),

             InlineKeyboardButton(text="VPN",
                                  url="https://medium.com/@alex.kach.2222/инструкция-по-настройке-vpn-dadace8dcb46")],

            # [InlineKeyboardButton(text="Принтеры",
            #                       url="https://dzen.ru")],

            [InlineKeyboardButton(text=l10n.format_value('back'),
                                  callback_data="menu_additionally"),

             InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return manuals


def get_settings(l10n):
    languages = get_settings_languages('from_settings')

    settings = InlineKeyboardMarkup(
        inline_keyboard=[
            [languages.inline_keyboard[0][i] for i in range(len(languages.inline_keyboard[0]))],

            [InlineKeyboardButton(text=l10n.format_value('change-mailing-time'),
                                  callback_data="change_mailing_time")],

            [InlineKeyboardButton(text=l10n.format_value('change-status-mailing'),
                                  callback_data="change_status_mailing")],

            [InlineKeyboardButton(text=l10n.format_value('change-status-numbers-in-menu'),
                                  callback_data="change_status_numbers_in_menu")],

            [InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return settings


def get_additionally_menu(l10n):
    additionally_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('menu-manuals-button'), callback_data="manuals")],
            [InlineKeyboardButton(text=l10n.format_value('menu-feedback-button'), callback_data="menu_feedback")],
            [InlineKeyboardButton(text=l10n.format_value('to-menu-main'), callback_data="menu_main")],
        ]
    )
    return additionally_menu


def get_feedback(l10n):
    feedback = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('contacts'),
                                  callback_data="contacts")],

            [InlineKeyboardButton(text=l10n.format_value('response'),
                                  callback_data="response")],

            [InlineKeyboardButton(text=l10n.format_value('back'),
                                  callback_data="menu_additionally"),
             InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")],
        ]
    )
    return feedback


def get_go_to(l10n, where):
    go_to = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('back'),
                                  callback_data=f"menu_{where}"),
             InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")]
        ]
    )
    return go_to


def get_go_to_menu_main(l10n):
    go_to_menu_main = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('to-menu-main'),
                                  callback_data="menu_main")]
        ]
    )
    return go_to_menu_main


def get_send_menu_main(l10n):
    send_menu_main = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('open-menu-main'), callback_data='send_menu_main')]
        ]
    )
    return send_menu_main


def get_status_send_feedback(l10n):
    status_send_feedback = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=l10n.format_value('send'), callback_data="feedback_send")],
            [InlineKeyboardButton(text=l10n.format_value('change'), callback_data="feedback_change")],
            [InlineKeyboardButton(text=l10n.format_value('cancel'), callback_data="feedback_cancel")]

        ]
    )
    return status_send_feedback


def get_settings_languages(where_was_called: str):
    settings_languages = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇷🇺", callback_data=f'settings_language_{where_was_called}_ru'),
             # InlineKeyboardButton(text="🇺🇦", callback_data=f'settings_language_{where_was_called}_uk'),
             InlineKeyboardButton(text="🇩🇪", callback_data=f'settings_language_{where_was_called}_de'),
             InlineKeyboardButton(text="🇺🇸", callback_data=f'settings_language_{where_was_called}_en')],

        ]
    )
    return settings_languages


def get_settings_language_from_start(l10n):
    languages = get_settings_languages('from_start')
    menu_main = get_send_menu_main(l10n)
    languages.inline_keyboard.append(menu_main.inline_keyboard[0])

    return languages











# admin_menu_logs = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="", callback_data="")]
#     ]
# )


# from fluent.runtime import FluentLocalization, FluentResourceLoader
#
# loader = FluentResourceLoader("locales/{locale}")
#
# l10n_en = FluentLocalization(["en"], ["base_en.ftl"], loader)
#
# get_settings_language_from_start(l10n_en)
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='main_menu',
            description='Главное меню'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
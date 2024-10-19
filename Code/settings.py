from commands.main_commands.info import Info
from aiogram import types
from aiogram.types import BotCommand

ROUTERS = [
    Info.router,
]

BOT_COMMANDS_LIST = [
    types.BotCommand(command='help', description='Подробное описание всех доступных команд'),
    types.BotCommand(command='start', description='Для использования бота'),
    types.BotCommand(command='echo', description='Копирует ваше сообщение после команды'),
]
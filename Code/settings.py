from commands.info import Start
from commands.do import MainCommands
from commands.settings_commands import router
from aiogram import types, Dispatcher
from aiogram.types import BotCommand

dp = Dispatcher()

ROUTERS = [router]

BOT_COMMANDS_LIST = [
    types.BotCommand(command='help', description='Подробное описание всех доступных команд'),
    types.BotCommand(command='do', description='Меню основного управления'),
    types.BotCommand(command='echo', description='Копирует ваше сообщение после команды'),
]
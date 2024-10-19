from commands.info import Start, Help
from aiogram import types, Dispatcher
from aiogram.types import BotCommand

dp = Dispatcher()

ROUTERS = [
    Start.router,
]

BOT_COMMANDS_LIST = [
    types.BotCommand(command='help', description='Подробное описание всех доступных команд'),
    types.BotCommand(command='echo', description='Копирует ваше сообщение после команды'),
]
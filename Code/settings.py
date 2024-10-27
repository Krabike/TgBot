#IT IS MANDATORY TO IMPORT 1 CLASS FROM EACH FILE WITH COMMANDS THAT YOU WANT TO ADD
from commands.diary.notes import GetNotes
from commands.info import Help
from commands.do import MainCommands
from commands.diary.diary import DiaryCommands
from commands.settings_commands import router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types, Dispatcher
from aiogram.types import BotCommand

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

ROUTERS = [router]

BOT_COMMANDS_LIST = [
    types.BotCommand(command='start', description='Меню основного управления'),
    types.BotCommand(command='help', description='Подробное описание всех доступных команд'),
    types.BotCommand(command='diary', description='Меню управление командами дневником'),
    types.BotCommand(command='cancel', description='Отменить ввод данных'),
    types.BotCommand(command='echo', description='Копирует ваше сообщение после команды'),
]
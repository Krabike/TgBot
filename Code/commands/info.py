from aiogram.types import Message
from aiogram.filters import Command
from .settings_commands import router
from .do import MainCommands
from .commands_data.my_data import MyHelp
import logging

class Help:
    #/help
    @router.message(Command('help'))
    async def help(message: Message):
        await message.answer(MyHelp.text_help, reply_markup = MyHelp.keyboard)
        
    #start button in help callback
    @router.callback_query(lambda call: call.data == 'type_start')
    async def help_callback(call):
        try:
            await MainCommands.start(call.message)
            await call.answer()
        except Exception as _ex:
            logging.error(f'start button in help callback: {_ex}')



class Echo:
    #/echo
    @router.message(Command("echo"))
    async def message_echo(message: Message):
        try:
            without_command = message.text.split(maxsplit=1)
            get_text = without_command[1]
            await message.answer(get_text)
        except:
            await message.answer("Обязательно значение после команды")
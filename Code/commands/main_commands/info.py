from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart
from aiogram import Router, html
from .settings_main_commands import COMMANDS_INFO
import logging


class Start:
    router = Router()

    @router.message(CommandStart())
    async def start(message: Message) -> None:
        start_message = f'Привет {html.bold(message.from_user.full_name)}, если хочешь узнать о возможностях бота - нажми на кнопку {html.bold('Help')}'
        start_button = InlineKeyboardButton(text='Help', callback_data='start_help')
        start_keyboard = InlineKeyboardMarkup(inline_keyboard = [[start_button]])
        await message.answer(start_message, reply_markup = start_keyboard)
    
    
    @router.callback_query(lambda call: call.data == 'start_help')    
    async def start_callback(call) -> None:
        try:
            if call.data == 'start_help':
                await Help.help(call.message)
                await call.answer()
        except:
            print('error with button info')




class Help(Start):
    router = Start.router

    @router.message(Command('help'))
    async def help(message: Message):
        answer_text = COMMANDS_INFO
        help_button = InlineKeyboardButton(text = 'Нажми чтобы начать', callback_data = 'type_start')
        help_keyboard = InlineKeyboardMarkup(inline_keyboard = [[help_button]])
        
        await message.answer(answer_text, reply_markup = help_keyboard)
        
    
    @router.callback_query(lambda call: call.data == 'type_start')
    async def help_callback(call) -> None:
        try:
            if call.data == 'type_start':
                await Start.start(call.message)
                await call.answer()
        except Exception as _ex:
            print(f'error with button help(start) {_ex}')



class Echo(Start):
    router = Start.router
    
    @router.message(Command("echo"))
    async def message_echo(message: Message) -> None:
        try:
            without_command = message.text.split(maxsplit=1)
            get_text = without_command[1]
            await message.answer(get_text)
        except:
            await message.answer("Input needed")
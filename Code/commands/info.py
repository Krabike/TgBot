from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart
from aiogram import html
from .settings_commands import COMMANDS_INFO, router
from .do import MainCommands
import logging


class Start:
    @router.message(CommandStart())
    async def start(message: Message):
        start_message = (
            f'Привет {html.bold(message.from_user.full_name)}, если хочешь узнать о возможностях бота - нажми на кнопку {html.bold('Help')}\n\n'
            f'А если сразу хочешь начать пользоваться ботом - нажми на {html.bold('Start')}'
            )
        start_button1 = InlineKeyboardButton(text='Help', callback_data='start_help')
        start_button2 = InlineKeyboardButton(text='Start', callback_data='start_start')
        start_keyboard = InlineKeyboardMarkup(inline_keyboard = [[start_button1, start_button2]])
        await message.answer(start_message, reply_markup = start_keyboard)
    
    
    @router.callback_query(lambda call: call.data == 'start_help')    
    async def start_help_callback(call):
        try:
            if call.data == 'start_help':
                await Help.help(call.message)
                await call.answer()
        except:
            print('error with button info')
            
    
    @router.callback_query(lambda call: call.data == 'start_start')
    async def start_start_callback(call):
        try:
            if call.data == 'start_start':
                await MainCommands.do(call.message)
                await call.answer()
        except Exception as _ex:
            print(f'error with button start {_ex}')




class Help:
    @router.message(Command('help'))
    async def help(message: Message):
        answer_text = COMMANDS_INFO
        help_button1 = InlineKeyboardButton(text = 'Нажми чтобы начать', callback_data = 'type_start')
        help_keyboard = InlineKeyboardMarkup(inline_keyboard = [[help_button1]])
        
        await message.answer(answer_text, reply_markup = help_keyboard)
        
    
    @router.callback_query(lambda call: call.data == 'type_start')
    async def help_callback(call):
        try:
            if call.data == 'type_start':
                await MainCommands.do(call.message)
                await call.answer()
        except Exception as _ex:
            print(f'error with button help(start) {_ex}')



class Echo:
    @router.message(Command("echo"))
    async def message_echo(message: Message):
        try:
            without_command = message.text.split(maxsplit=1)
            get_text = without_command[1]
            await message.answer(get_text)
        except:
            await message.answer("Обязательно значение после команды")
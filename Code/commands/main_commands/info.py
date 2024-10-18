from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart
from aiogram import Router, html
import logging


class Info:
    router = Router()

    @router.message(CommandStart())
    async def start(message: Message) -> None:
        msg = f'Привет {html.bold(message.from_user.full_name)}, если хочешь узнать о возможностях бота - нажми на кнопку {html.bold('Info')}'
        btn = InlineKeyboardButton(text='Info', callback_data='info')
        keyboard = InlineKeyboardMarkup(inline_keyboard = [[btn]])
        await message.answer(msg, reply_markup = keyboard)
    
    
    @router.callback_query()    
    async def start_callback(call) -> None:
        try:
            if call.data == 'info':
                await call.message.answer('just a couple of information')
                await call.answer()
        except:
            print('error with button info')
    



class Echo(Info):
    router = Info.router
    
    @router.message(Command("echo"))
    async def message_echo(message: Message) -> None:
        try:
            without_command = message.text.split(maxsplit=1)
            get_text = without_command[1]
            await message.answer(get_text)
        except:
            await message.answer("Input needed")
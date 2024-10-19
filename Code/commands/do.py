from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command
from aiogram import html
from .settings_commands import router
import logging

class MainCommands:
    #DO
    @router.message(Command('do'))
    async def do(message: Message):
        do_button1 = InlineKeyboardButton(text = 'Test Button', callback_data = 'do_btn1')
        do_keyboard = InlineKeyboardMarkup(inline_keyboard=[[do_button1]])
        await message.answer('просто текст...', reply_markup = do_keyboard)
        
    #DO CALlBACK
    @router.callback_query(lambda call: call.data == 'do_btn1')
    async def do_callback(call):
        try:
            if call.data == 'do_btn1':
                edited_do_button1 = InlineKeyboardButton(text = 'Next Button', callback_data = 'edited_do_btn1')
                edited_do_keyboard = InlineKeyboardMarkup(inline_keyboard=[[edited_do_button1]])
                await call.message.edit_text(text = 'edited...', reply_markup = edited_do_keyboard)
                await call.answer()
        except Exception as _ex:
            print(f'error with button help(start) {_ex}')
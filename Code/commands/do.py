from aiogram.types import Message
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command, CommandStart
from aiogram import html
from .settings_commands import router
from .commands_data.my_data import CommandDo, Diary
import logging

class MainCommands:
    #start
    @router.message(CommandStart())
    async def start(message: Message):
        await message.answer(CommandDo.text_start, reply_markup = CommandDo.keyboard)
  

    #start callback diary button
    @router.callback_query(lambda call: call.data == 'do_btn_diary')
    async def do_option1_callback(call):
        try:
            if call.data == 'do_btn_diary':
                await call.message.edit_text(text = Diary.text_start, reply_markup = Diary.keyboard)
                await call.answer()
        except Exception as _ex:
            print(f'error with button help(start) {_ex}')
from aiogram.types import Message
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command
from aiogram import html
from .settings_commands import router
from .commands_data.my_data import CommandDo, Notion
import logging

class MainCommands:
    #DO
    @router.message(Command('do'))
    async def do(message: Message):
        await message.answer(CommandDo.text_start, reply_markup = CommandDo.keyboard)
  

    #DO CALlBACK NOTION BUTTON
    @router.callback_query(lambda call: call.data == 'do_btn_notion')
    async def do_option1_callback(call):
        try:
            if call.data == 'do_btn_notion':
                await call.message.edit_text(text = Notion.text_start, reply_markup = Notion.keyboard)
                await call.answer()
        except Exception as _ex:
            print(f'error with button help(start) {_ex}')
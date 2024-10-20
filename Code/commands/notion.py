from aiogram.types import Message
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command
from aiogram import html
from .settings_commands import router
from .commands_data.my_data import CommandDo, Notion
import logging


class NotionCommands:
    #NOTION COMMAND
    @router.message(Command('notion'))
    async def do(message: Message):
        await message.answer(Notion.text_start, reply_markup = Notion.keyboard)
    
    
    #NOTION BACK CALLBACK
    @router.callback_query(lambda call: call.data == 'notion_btn_back')
    async def option1_back_callback(call):
        try:
            if call.data == 'notion_btn_back':
                await call.message.edit_text(text = CommandDo.text_start, reply_markup = CommandDo.keyboard)
                await call.answer()
        except Exception as _ex:
            print(f'error option1_btn_back callback {_ex}')
            
    
    #NOTION BUTTON1 CALLBACK
    @router.callback_query(lambda call: call.data == 'notion_btn1')
    async def option1_btn1_callback(call):
        try:
            if call.data == 'notion_btn1':
                await call.message.answer(Notion.text_btn1)
                await call.answer()
        except Exception as _ex:
            print(f'error notion_btn1 callback {_ex}')
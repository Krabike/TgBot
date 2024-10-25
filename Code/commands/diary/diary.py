from aiogram.types import Message
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command
from aiogram import html
from ..settings_commands import router
from ..commands_data.my_data import CommandDo, Diary
from .diary_parser import DiaryNotes
import logging


class DiaryCommands:
    #/diary
    @router.message(Command('diary'))
    async def diary(message: Message):
        await message.answer(Diary.text_start, reply_markup = Diary.keyboard)
    
    
    #diary back callback
    @router.callback_query(lambda call: call.data == 'diary_notes_back')
    async def diary_back_callback(call):
        try:
            if call.data == 'diary_notes_back':
                await call.message.edit_text(text = CommandDo.text_start, reply_markup = CommandDo.keyboard)
                await call.answer()
        except Exception as _ex:
            print(f'error option1_btn_back callback {_ex}')
            
    
    #diary get notes callback
    @router.callback_query(lambda call: call.data == 'diary_notes')
    async def diary_notes_callback(call):
        try:
            if call.data == 'diary_notes':
                await call.message.answer(f"{DiaryNotes().notes()}", parse_mode="Markdown")
                await call.answer()
        except Exception as _ex:
            print(f'error diary_btn1 callback {_ex}')
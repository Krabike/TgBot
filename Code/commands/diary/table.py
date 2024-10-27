from supabase import create_client, Client
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from ..settings_commands import router
from ..commands_data.my_data import CommandDo, Diary, ChangeWeek
from .diary_parser import DiaryNotes
from .db_connection import DBConnection
from configs.config import db_url, db_key
import logging

class Table:
    @router.callback_query(lambda call: call.data == 'table')
    async def diary_notes_callback(call):
        try:
            
            
            await call.message.answer()
            await call.answer()
        except Exception as _ex:
            await call.message.answer('ошибка')
            await call.answer()
            logging.error(f'cant receive notes in get notes button callback: {_ex}')
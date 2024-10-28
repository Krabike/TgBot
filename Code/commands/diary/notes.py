from supabase import create_client, Client
from aiogram.exceptions import TelegramBadRequest
from ..settings_commands import router
from ..commands_data.my_data import ChangeWeek
from .diary_parser import DiaryNotes
from .db_connection import DBConnection
from configs.config import db_url, db_key
import logging


supabase: Client = create_client(db_url, db_key)


#get notes callback
class GetNotes:
    week_count = 0
    @router.callback_query(lambda call: call.data == 'notes')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            
            await call.message.answer(f"{DiaryNotes(f'{login}', f'{password}').notes()}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except Exception as _ex:
            await call.message.answer('Данные для входа неверны или не указаны')
            await call.answer()
            logging.error(f'cant receive notes in get notes button callback: {_ex}')
            

#PREVIOUS WEEK
    @router.callback_query(lambda call: call.data == 'btn_prev')
    async def prev_week_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            GetNotes.week_count += 1
            
            await call.message.edit_text(f"{DiaryNotes(f'{login}', f'{password}').notes(week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.message.answer('Данные для входа неверны или не указаны')
            await call.answer()
            logging.error(f'previous week button callback: {_ex}')


#ZERO WEEK
    @router.callback_query(lambda call: call.data == 'btn_zeroweek')
    async def prev_week_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            GetNotes.week_count = 0
            
            await call.message.edit_text(f"{DiaryNotes(f'{login}', f'{password}').notes(week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except Exception as _ex:
            if GetNotes.week_count == 0:
                await call.answer('Вы уже на начальной странице')
                await call.answer()
            else:
                await call.message.answer('Данные для входа неверны или не указаны')
                await call.answer()
                logging.error(f'zero week button callback: {_ex}')


#NEXT WEEK
    @router.callback_query(lambda call: call.data == 'btn_next')
    async def prev_week_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            GetNotes.week_count -= 1
            
            await call.message.edit_text(f"{DiaryNotes(f'{login}', f'{password}').notes(week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.message.answer('Данные для входа неверны или не указаны')
            await call.answer()
            logging.error(f'next week button callback: {_ex}')
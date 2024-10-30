from aiogram.exceptions import TelegramBadRequest
from aiogram import F
from ..settings_commands import router
from ..commands_data.my_data import ChangeWeek, Diary
from .async_parser import NotesParser
from .db_connection import DBConnection
import logging


#get notes callback
class GetNotes:
    week_count = 0
    @router.callback_query(F.data == 'notes')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            await call.message.edit_text(f"{await NotesParser().parser(f'{data_db[0]}', f'{data_db[1]}')}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.answer('Неверные данные')
            logging.error(f'cant receive notes in get notes button callback: {_ex}')
            
            
    @router.callback_query(F.data == 'btn_back_change_week')
    async def diary_notes_callback(call):
        try:
            await call.message.edit_text(Diary.text_start, reply_markup = Diary.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.answer()
            logging.error(f'change week back button callback: {_ex}')        
            

#PREVIOUS WEEK
    @router.callback_query(F.data == 'btn_prev')
    async def prev_week_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            GetNotes.week_count += 1
            
            await call.message.edit_text(f"{await NotesParser().parser(f'{data_db[0]}', f'{data_db[1]}', week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.answer('Неверные данные')
            logging.error(f'previous week button callback: {_ex}')


#ZERO WEEK
    @router.callback_query(F.data == 'btn_zeroweek')
    async def prev_week_callback(call):
        try:
            if GetNotes.week_count == 0:
                await call.answer('Вы уже на начальной странице')
            else:
                user_id = call.from_user.id
                data_db = await DBConnection().take_login_password_db(user_id)
                GetNotes.week_count = 0
            
                await call.message.edit_text(f"{await NotesParser().parser(f'{data_db[0]}', f'{data_db[1]}', week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
                await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
                await call.answer('Неверные данные')
                logging.error(f'zero week button callback: {_ex}')


#NEXT WEEK
    @router.callback_query(F.data == 'btn_next')
    async def prev_week_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            GetNotes.week_count -= 1
            
            await call.message.edit_text(f"{await NotesParser().parser(f'{data_db[0]}', f'{data_db[1]}', week = GetNotes.week_count)}", parse_mode="Markdown", reply_markup = ChangeWeek.keyboard)
            await call.answer()
        except TelegramBadRequest:
            await call.answer()
        except Exception as _ex:
            await call.answer('Неверные данные')
            logging.error(f'next week button callback: {_ex}')
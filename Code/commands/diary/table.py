from ..settings_commands import router
from ..commands_data.my_data import Diary, Homework
from .db_connection import DBConnection
from .async_table import TableParser
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from aiogram import F
import logging


class Table:
    week_count = 0
    #table button in diary
    @router.callback_query(F.data == 'table')
    async def diary_notes_callback(call):
        try:
            await call.message.edit_text(text=Homework.text+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', reply_markup=Homework.keyboard, parse_mode = 'Markdown')
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table button callback: {_ex}')
            
            
    #BACK BUTTON
    @router.callback_query(F.data == 'btn_homework_back')
    async def diary_notes_callback(call):
        try:
            await call.message.edit_text(text=Diary.text_start, reply_markup=Diary.keyboard)
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'back button in table callback: {_ex}')
    
    
    #monday button
    @router.callback_query(F.data == 'btn_monday')
    async def diary_notes_callback(call: CallbackQuery):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Пн'
            text = await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)
            await call.message.edit_text(text+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest as _ex:
            print(f'word {_ex}')
            call.answer('d')
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table monday button callback: {_ex}')
        
    
    #tuesday button
    @router.callback_query(F.data == 'btn_tuesday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Вт'
            await call.message.edit_text(f"{await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)}"+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table tuesday button callback: {_ex}')
        
        
    #wednesday button
    @router.callback_query(F.data == 'btn_wednesday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Ср'       
            await call.message.edit_text(f"{await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)}"+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table wednesday button callback: {_ex}')
        
        
    #thursday button
    @router.callback_query(F.data == 'btn_thursday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Чт'
            await call.message.edit_text(f"{await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)}"+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table thursday button callback: {_ex}')
            
            
    #friday button
    @router.callback_query(F.data == 'btn_friday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Пт'
            await call.message.edit_text(f"{await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)}"+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table friday button callback: {_ex}')
            
            
    #sunday button
    @router.callback_query(F.data == 'btn_sunday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            data_db = await DBConnection().take_login_password_db(user_id)
            
            day = 'Сб'
            await call.message.edit_text(f"{await TableParser().parser(f'{data_db[0]}', f'{data_db[1]}', day, Table.week_count)}"+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', parse_mode="Markdown", reply_markup=Homework.keyboard)
            await call.answer()
        except TelegramBadRequest:
            call.answer()
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'table friday button callback: {_ex}')
            
    
    #prev button callback
    @router.callback_query(F.data == 'btn_prev_table')
    async def diary_notes_callback(call):
        try:
            Table.week_count += 1
            await call.message.edit_text(text=Homework.text+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', reply_markup=Homework.keyboard, parse_mode = 'Markdown')
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'prev button in table callback: {_ex}')
    
    
    #zero button callback
    @router.callback_query(F.data == 'btn_zeroweek_table')
    async def diary_notes_callback(call):
        try:
            if Table.week_count == 0:
                await call.answer(f'Неделя уже {Table.week_count}')
            else:
                Table.week_count = 0
                await call.message.edit_text(text=Homework.text+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', reply_markup=Homework.keyboard, parse_mode = 'Markdown')
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'zero button in table callback: {_ex}')
            
            
    #next button callback
    @router.callback_query(F.data == 'btn_next_table')
    async def diary_notes_callback(call):
        try:
            Table.week_count -= 1
            await call.message.edit_text(text=Homework.text+f'\nНеделя на которой вы находитесь: `{Table.week_count}`', reply_markup=Homework.keyboard, parse_mode = 'Markdown')
        except Exception as _ex:
            await call.answer('Нет заданий')
            logging.error(f'next button in table callback: {_ex}')
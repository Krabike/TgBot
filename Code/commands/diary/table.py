from ..settings_commands import router
from ..commands_data.my_data import Diary, Homework
from .db_connection import DBConnection
from .table_parser import TableParser
import logging


class Table:
    #table button in diary
    @router.callback_query(lambda call: call.data == 'table')
    async def diary_notes_callback(call):
        try:
            await call.message.edit_text(text=Homework.text, reply_markup=Homework.keyboard, parse_mode = 'Markdown')
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table button callback: {_ex}')
            
            
    #BACK BUTTON
    @router.callback_query(lambda call: call.data == 'btn_homework_back')
    async def diary_notes_callback(call):
        try:
            await call.message.edit_text(text=Diary.text_start, reply_markup=Diary.keyboard)
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'back button in table callback: {_ex}')
    
    
    #monday button
    @router.callback_query(lambda call: call.data == 'btn_monday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            day = 'Пн'
            await call.message.edit_text(f"{TableParser(f'{login}', f'{password}').table(day)}", parse_mode="Markdown", reply_markup=Homework.keyboard_monday)
            await call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table monday button callback: {_ex}')
        
    
    #tuesday button
    @router.callback_query(lambda call: call.data == 'btn_tuesday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            day = 'Вт'
            await call.message.edit_text(f"{TableParser(f'{login}', f'{password}').table(day)}", parse_mode="Markdown", reply_markup=Homework.keyboard_tuesday)
            await call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table tuesday button callback: {_ex}')
        
        
    #wednesday button
    @router.callback_query(lambda call: call.data == 'btn_wednesday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            day = 'Ср'       
            await call.message.edit_text(f"{TableParser(f'{login}', f'{password}').table(day)}", parse_mode="Markdown", reply_markup=Homework.keyboard_wednesday)
            await call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table wednesday button callback: {_ex}')
        
        
    #thursday button
    @router.callback_query(lambda call: call.data == 'btn_thursday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            day = 'Чт'
            await call.message.edit_text(f"{TableParser(f'{login}', f'{password}').table(day)}", parse_mode="Markdown", reply_markup=Homework.keyboard_thursday)
            await call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table thursday button callback: {_ex}')
            
            
    #friday button
    @router.callback_query(lambda call: call.data == 'btn_friday')
    async def diary_notes_callback(call):
        try:
            user_id = call.from_user.id
            password = await DBConnection().take_password_db(user_id)
            login = await DBConnection().take_login_db(user_id)
            
            day = 'Пт'
            await call.message.edit_text(f"{TableParser(f'{login}', f'{password}').table(day)}", parse_mode="Markdown", reply_markup=Homework.keyboard_friday)
            await call.answer()
        except Exception as _ex:
            await call.answer('Ошибка')
            logging.error(f'table friday button callback: {_ex}')
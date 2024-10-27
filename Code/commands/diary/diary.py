from supabase import create_client, Client
from aiogram.types import Message
from aiogram.methods.edit_message_caption import EditMessageCaption
from aiogram.filters import Command
from aiogram import html
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from ..settings_commands import router
from ..commands_data.my_data import CommandDo, Diary
from .diary_parser import DiaryNotes
#from configs.config import db_url, db_key
import os
import logging


supabase: Client = create_client(os.getenv('DB_URL'), os.getenv('DB_KEY'))


class Reg(StatesGroup):
    login = State()
    password = State()


class DiaryCommands:
    #/diary
    @router.message(Command('diary'))
    async def diary(message: Message):
        await message.answer(Diary.text_start, reply_markup = Diary.keyboard)
    
    
    #diary back callback
    @router.callback_query(lambda call: call.data == 'diary_notes_back')
    async def diary_back_callback(call):
        try:
            await call.message.edit_text(text = CommandDo.text_start, reply_markup = CommandDo.keyboard)
            await call.answer()
        except Exception as _ex:
            print(f'error option1_btn_back callback {_ex}')
            
    
    #diary get notes callback
    @router.callback_query(lambda call: call.data == 'diary_notes')
    async def diary_notes_callback(call):
        try:
            try:
                user_id = call.from_user.id
                
                response = (
                supabase.table("TgUsers")
                .select("login, password")
                .eq("user_id", user_id)
                .execute()
                )
                
                login = response.data[0]["login"]
                password = response.data[0]["password"]
                
                print(login, password)
                
                await call.message.answer(f"{DiaryNotes(f'{login}', f'{password}').notes()}", parse_mode="Markdown")
                await call.answer()
            except Exception as _ex:
                await call.message.answer('Данные для входа указаны неправильно или вовсе не указаны')
                await call.answer()
                logging.error(f'ошибка при получении оценок{_ex}')
        except Exception as _ex:
            print(f'error diary_btn1 callback {_ex}')
            
    
    #diary sign_in callback
    @router.callback_query(lambda call: call.data == 'diary_sign_in')
    async def diary_sign_in_callback(call, state: FSMContext):
        try:
            user_id = call.from_user.id
            existing_user = (
                supabase.table("TgUsers")
                .select("*")
                .eq("user_id", user_id)
                .execute()
            )
            
            if existing_user.data:
                await call.message.answer("Пользователь уже существует")
                await call.answer()
            else:    
                await state.set_state(Reg.login)
                await call.message.answer('Введите *логин* от электронного дневника\n\nЕсли вы хотите это отменить напишите */cancel*', parse_mode="Markdown")
                await call.answer()
            
        except Exception as _ex:
            print(f'error sign_in callback {_ex}')
            



class Login:
    #/cancel
    @router.message(Command('cancel'))
    async def cancel(message: Message, state: FSMContext):
        current_state = await state.get_state() 
        if current_state:
            await state.clear()
            await message.answer('Успешная отмена')
        else:
            await message.answer('Мне нечего отменять')
        
    
    @router.message(Reg.login)
    async def login_state(message: Message, state: FSMContext):
        await state.update_data(login=message.text)
        await state.set_state(Reg.password)
        await message.answer('Введите *пароль* от электронного дневника\n\nЕсли вы хотите это отменить напишите */cancel*', parse_mode="Markdown")
        
    
    @router.message(Reg.password)
    async def password_state(message: Message, state: FSMContext):
        await state.update_data(password=message.text)
        data = await state.get_data()
        user_login = data["login"]
        user_password = data["password"]
        
        user_id = message.from_user.id
        
        try:
            db_response = (
                supabase.table("TgUsers")
                .insert({"login": user_login, "password": user_password, "user_id": user_id})
                .execute()
            )
            await message.answer(f'Успешное внесение данных\nlogin: {user_login},\npassword: {user_password}')
        except Exception as _ex:
            logging.error(f"Error saving to database: {_ex}")
            await message.answer("Не удалось сохрнаить данные в базу данных")
            
        await state.clear()
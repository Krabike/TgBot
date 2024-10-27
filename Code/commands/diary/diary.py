from supabase import create_client, Client
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from ..settings_commands import router
from ..commands_data.my_data import CommandDo, Diary
from .diary_parser import DiaryNotes
from configs.config import db_url, db_key
import logging


supabase: Client = create_client(db_url, db_key)


class Reg(StatesGroup):
    login = State()
    password = State()


class ChangeReg(StatesGroup):
    change_login = State()
    change_password = State()


class DiaryCommands:
    #/diary
    @router.message(Command('diary'))
    async def diary(message: Message):
        await message.answer(Diary.text_start, reply_markup = Diary.keyboard)
    
    
    #back callback
    @router.callback_query(lambda call: call.data == 'diary_back')
    async def diary_back_callback(call):
        try:
            await call.message.edit_text(text = CommandDo.text_start, reply_markup = CommandDo.keyboard)
            await call.answer()
        except Exception as _ex:
            logging.error(f'back button callback in diary: {_ex}')
            
    
    #get notes callback
    @router.callback_query(lambda call: call.data == 'notes')
    async def diary_notes_callback(call):
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
                
                
            await call.message.answer(f"{DiaryNotes(f'{login}', f'{password}').notes()}", parse_mode="Markdown")
            await call.answer()
        except Exception as _ex:
            await call.message.answer('Данные для входа неверны или не указаны')
            await call.answer()
            logging.error(f'cant receive notes in get notes button callback: {_ex}')
            
    
    #sign_in callback
    @router.callback_query(lambda call: call.data == 'sign_in')
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
                await state.set_state(ChangeReg.change_login)
                await call.answer('Смена аккаунта')
                await call.message.answer('Введите *новый логин*\nЕсли вы хотите отменить ввод - напишите */cancel*', parse_mode="Markdown")
                await call.answer()
            else:    
                await state.set_state(Reg.login)
                await call.answer('Добавление аккаунта')
                await call.message.answer('Введите *логин* от электронного дневника\nЕсли вы хотите отменить ввод - напишите */cancel*', parse_mode="Markdown")
                await call.answer()
            
        except Exception as _ex:
            logging.error(f'sign in button callback: {_ex}')



class ChangeLogin:
    @router.message(ChangeReg.change_login)
    async def login_change(message: Message, state: FSMContext):
        await state.update_data(change_login=message.text)
        await state.set_state(ChangeReg.change_password)
        await message.answer('Введите *новый пароль*\nЕсли вы хотите отменить ввод - напишите */cancel*', parse_mode="Markdown")
        
        
    @router.message(ChangeReg.change_password)
    async def login_change(message: Message, state: FSMContext):
        await state.update_data(change_password=message.text)
        change_data = await state.get_data()
        changed_user_login = change_data["change_login"]
        changed_user_password = change_data["change_password"]
        
        user_id = message.from_user.id
        
        try:
            db_response = (
                supabase.table("TgUsers")
                .update({"login": changed_user_login, "password": changed_user_password})
                .eq("user_id", user_id)
                .execute()
            )
            await message.answer(f'*Успешное изменение данных*\nЛогин: `{changed_user_login}`\nПароль: `{changed_user_password}`', parse_mode="Markdown")
        except Exception as _ex:
            logging.error(f"cant change data in database: {_ex}")
            await message.answer("Не удалось изменить данные")
            
        await state.clear()



class Login:
    @router.message(Reg.login)
    async def login_state(message: Message, state: FSMContext):
        await state.update_data(login=message.text)
        await state.set_state(Reg.password)
        await message.answer('Введите *пароль* от электронного дневника\nЕсли вы хотите отменить ввод - напишите */cancel*', parse_mode="Markdown")
        
    
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
            await message.answer(f'*Успешное внесение данных*\nЛогин: `{user_login}`\nПароль: `{user_password}`', parse_mode="Markdown")
        except Exception as _ex:
            logging.error(f"cant save data to database: {_ex}")
            await message.answer("Не удалось сохрнаить данные")
            
        await state.clear()
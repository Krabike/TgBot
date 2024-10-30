from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import F
from .settings_commands import router
from .commands_data.my_data import CommandDo, Diary
import logging

class MainCommands:
    #/start
    @router.message(CommandStart())
    async def start(message: Message):
        await message.answer(CommandDo.text_start, reply_markup = CommandDo.keyboard)
    
    
    #/cancel
    @router.message(Command('cancel'))
    async def cancel(message: Message, state: FSMContext):
        current_state = await state.get_state() 
        if current_state:
            await state.clear()
            await message.answer('Успешная отмена')
        else:
            await message.answer('Мне нечего отменять')
  

    #start callback diary button
    @router.callback_query(F.data == 'do_btn_diary')
    async def do_option1_callback(call):
        try:
            await call.message.edit_text(text = Diary.text_start, reply_markup = Diary.keyboard)
            await call.answer()
        except Exception as _ex:
            logging.error(f'diary button callback: {_ex}')
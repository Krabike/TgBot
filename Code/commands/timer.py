from aiogram.types import Message
from aiogram.filters import Command
from .settings_commands import router
import asyncio

class ClosedTimer:
    @router.message(Command('timer'))
    async def timer(message: Message):
        try:
            if message.from_user.id == 1040778722:
                without_command = message.text.split(maxsplit=1)
                get_number = float(without_command[1])
                await message.answer(f'Timer `set` {get_number}h', parse_mode='Markdown')
                await asyncio.sleep(get_number*3600)
                await message.answer(f'*Timeout {get_number/3600}:*\ntake a `break` at least 20 minutes', parse_mode='Markdown')
        except:
            await message.answer('*Установи время* для таймера `после команды`', parse_mode='Markdown')
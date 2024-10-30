from settings import ROUTERS, BOT_COMMANDS_LIST, dp
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from configs.config import token
import asyncio
import logging
import sys

logger = logging.getLogger("my_app")

async def main():
    bot = Bot(token = token, default = DefaultBotProperties(parse_mode = ParseMode.HTML))
    dp.include_routers(*ROUTERS)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(BOT_COMMANDS_LIST)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.warning('Bot started')
    asyncio.run(main())
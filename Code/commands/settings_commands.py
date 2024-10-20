from aiogram import Router


router = Router()


COMMANDS_INFO = (
    'Все доступные команды:\n\n'
    '/help - выводит это сообщение\n'
    '/echo - выводит текст, введенный после команды\n'
    '/do - меню с основным управлением ботом\n'
    '/notion - меню управления командами Notion\n'
)
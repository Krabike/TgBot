from aiogram import Router, html


router = Router()


COMMANDS_INFO = (
    f'{html.bold(html.underline("Все доступные команды:"))}\n\n'
    f'{html.italic(html.underline("/start"))} - меню с основным управлением ботом\n'
    f'{html.italic(html.underline("/help"))} - выводит это сообщение\n'
    f'{html.italic(html.underline("/diary"))} - меню управления командами дневника\n'
    f'{html.italic(html.underline("/cancel"))} - отменить ввод данных\n'
    f'{html.italic(html.underline("/echo"))} - выводит текст после команды\n'
    f'\n ➠ {html.bold(html.link("Source code", "https://github.com/Krabike/TgBot"))}'
)
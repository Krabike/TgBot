from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import html
from ..settings_commands import COMMANDS_INFO


class MyHelp:
    text_help = COMMANDS_INFO
    
    help_button1 = InlineKeyboardButton(text = 'Нажми чтобы начать', callback_data = 'type_start')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard = [[help_button1]])


class CommandDo:
    #command /do
    text_start = (
        f'{html.bold("Меню выбора основных разделов")}\n'
        f'{html.underline("Дневник")} - управление дневником\n'
        f'\n{html.bold("Если нужна помощь")}\n'
        f'{html.bold(html.underline("/help"))} - вывод сообщения со всеми командами и описанием бота\n'
    )
    
    button_diary = InlineKeyboardButton(text = 'Дневник', callback_data = 'do_btn_diary')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_diary]])
    
    
class Diary:    
    #Diary buttons
    text_start = (
        f'{html.bold("Меню выбора команд дневника")}\n'
        f'{html.underline("Оценки")} - вывод оценок за текущую неделю\n'
        f'{html.underline("Войти в аккаунт")} - вход и изменение данных от электронного дневника\n'
        f'{html.underline("Назад")} - возвращение к предыдущему сообщению\n'
        f'\n{html.bold("Если не работает кнопка с оценками")}\n'
        'Если у вас не привязан аккаунт к гос. услугам, то для получения списка с оценками нужно раз в несколько часов заходить в дневник и нажимать "напомнить позже" на сообщение с просьбой привязать гос. услуги\n'
    )
    
    button_notes = InlineKeyboardButton(text = 'Оценки', callback_data = 'notes')
    button_table = InlineKeyboardButton(text = 'Расписание', callback_data = 'table')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'diary_back')
    button_sign_in = InlineKeyboardButton(text = 'Войти в аккаунт', callback_data = 'sign_in')
    
    keyboard = InlineKeyboardMarkup(row_width=3, inline_keyboard=[[button_notes, button_table], [button_sign_in], [button_back]])


class ChangeWeek:
    #swap week

    button_prev = InlineKeyboardButton(text = '⬅️', callback_data = 'btn_prev')
    button_zeroweek = InlineKeyboardButton(text = '🔄', callback_data = 'btn_zeroweek')
    button_next =InlineKeyboardButton(text = '➡️', callback_data = 'btn_next')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_prev, button_zeroweek, button_next]])


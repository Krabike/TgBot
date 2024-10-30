from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import html


class MyHelp:
    text_help =(
    f'{html.bold(html.underline("Все доступные команды:"))}\n\n'
    f'{html.italic(html.underline("/start"))} - меню с основным управлением ботом\n'
    f'{html.italic(html.underline("/help"))} - выводит это сообщение\n'
    f'{html.italic(html.underline("/diary"))} - меню управления командами дневника\n'
    f'{html.italic(html.underline("/cancel"))} - отменить ввод данных\n'
    f'{html.italic(html.underline("/echo"))} - выводит текст после команды\n'
    f'\n ➠ {html.bold(html.link("Source code", "https://github.com/Krabike/TgBot"))}'
    )
    
    help_button1 = InlineKeyboardButton(text = 'Нажмите чтобы начать', callback_data = 'type_start')
    
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
        f'{html.underline("Расписание")} - вывод домашнего задания за текущую неделю\n'
        f'{html.underline("Аккаунт")} - вход и изменение данных от электронного дневника\n'
        f'{html.underline("Назад")} - возвращение к предыдущему сообщению\n'
    )
    
    button_notes = InlineKeyboardButton(text = 'Оценки', callback_data = 'notes')
    button_table = InlineKeyboardButton(text = 'Расписание', callback_data = 'table')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'diary_back')
    button_sign_in = InlineKeyboardButton(text = 'Аккаунт', callback_data = 'sign_in')
    
    keyboard = InlineKeyboardMarkup(row_width=3, inline_keyboard=[[button_notes, button_table], [button_sign_in], [button_back]])


class ChangeWeek:
    #swap week

    button_prev = InlineKeyboardButton(text = '⬅️', callback_data = 'btn_prev')
    button_zeroweek = InlineKeyboardButton(text = '🔄', callback_data = 'btn_zeroweek')
    button_next = InlineKeyboardButton(text = '➡️', callback_data = 'btn_next')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'btn_back_change_week')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_prev, button_zeroweek, button_next], [button_back]])


class Homework:
    #days in homework button
    text = '*Выберите день недели, в котором хотите посмотреть домашнее задание*\n'
    
    button_monday = InlineKeyboardButton(text = 'Понедельник', callback_data = 'btn_monday')
    button_tuesday = InlineKeyboardButton(text = 'Вторник', callback_data = 'btn_tuesday')
    button_wednesday = InlineKeyboardButton(text = 'Среда', callback_data = 'btn_wednesday')
    button_thursday = InlineKeyboardButton(text = 'Четверг', callback_data = 'btn_thursday')
    button_friday = InlineKeyboardButton(text = 'Пятница', callback_data = 'btn_friday')
    button_sunday = InlineKeyboardButton(text = 'Суббота', callback_data = 'btn_sunday')
    
    button_prev = InlineKeyboardButton(text = '⬅️', callback_data = 'btn_prev_table')
    button_zeroweek = InlineKeyboardButton(text = '🔄', callback_data = 'btn_zeroweek_table')
    button_next = InlineKeyboardButton(text = '➡️', callback_data = 'btn_next_table')
    
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'btn_homework_back')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_monday, button_tuesday, button_wednesday], [button_thursday, button_friday, button_sunday], [button_prev, button_zeroweek, button_next], [button_back]])
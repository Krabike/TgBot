from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CommandDo:
    #command /do
    text_start = 'Это стартовое сообщение\nМеню выбора:'
    
    button_option_notion = InlineKeyboardButton(text = 'Дневник', callback_data = 'do_btn_diary')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_option_notion]])
    
    
class Diary:    
    #Notion buttons
    text_start = 'Меню выбора дневника...'
    text_btn1 = 'just a work text'
    
    button1 = InlineKeyboardButton(text = 'Оценки за неделю', callback_data = 'diary_notes')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'diary_notes_back')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button_back]])
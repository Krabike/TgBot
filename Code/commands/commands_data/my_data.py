from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CommandDo:
    #command /do
    text_start = 'Это стартовое сообщение\nМеню выбора:'
    
    button_option_notion = InlineKeyboardButton(text = 'Notion', callback_data = 'do_btn_notion')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_option_notion]])
    
    
class Notion:    
    #option1 buttons
    text_start = 'Notion меню выбора...'
    text_btn1 = 'just a work text'
    
    button1 = InlineKeyboardButton(text = 'Сделать что-то', callback_data = 'notion_btn1')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'notion_btn_back')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button_back]])
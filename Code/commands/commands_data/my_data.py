from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class CommandDo:
    #command /do
    text_start = 'Это стартовое сообщение\nМеню выбора:'
    
    button_option_notion = InlineKeyboardButton(text = 'Дневник', callback_data = 'do_btn_diary')
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_option_notion]])
    
    
class Diary:    
    #Diary buttons
    text_start = 'Меню выбора дневника...'
    
    button1 = InlineKeyboardButton(text = 'Оценки за неделю', callback_data = 'diary_notes')
    button_back = InlineKeyboardButton(text = 'Назад', callback_data = 'diary_notes_back')
    button_sign_in = InlineKeyboardButton(text = 'Войти в аккаунт', callback_data = 'diary_sign_in')
    button_sign_in_change = InlineKeyboardButton(text = 'Изменить аккаунт', callback_data = 'diary_sign_in_change')
    
    keyboard = InlineKeyboardMarkup(row_width=3, inline_keyboard=[[button1], [button_sign_in, button_sign_in_change], [button_back]])

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Переписать текст"), KeyboardButton(text="Анализ текста")],
        [KeyboardButton(text="Рерайт"), KeyboardButton(text="Показать статистику")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)
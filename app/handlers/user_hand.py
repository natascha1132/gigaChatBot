from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app.lexicon.lexicon import LEXICON
from aiogram import types
from app.database.database import Database
from app.globals import database
from app.keyboards.key_words import main_menu

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_command(message: types.Message, main_menu: types.ReplyKeyboardMarkup, database: Database):
    user_id = message.from_user.id
    username = message.from_user.username
    database.add_user(user_id, username, state=None)
    await message.answer(
        "Привет! Я бот для работы с текстами. Выберите действие в меню.",
        reply_markup=main_menu
    )

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def help_command(message: types.Message):
    await message.answer(LEXICON["help"])

# Этот хэндлер срабатывает на команду /admin
@router.message(Command(commands='admin'))
async def admin_command(message: types.Message):
    if message.from_user.id == 1139579739:
        stats = database.get_all_user_statistics()
        stats_text = "\n".join(
            [f"Пользователь {stat['user_id']}: {stat['requests_count']} запросов" for stat in stats]
        )
        await message.answer(f"Общая статистика:\n{stats_text}")
    else:
        await message.answer("У Вас нет доступа к админ-панели.")


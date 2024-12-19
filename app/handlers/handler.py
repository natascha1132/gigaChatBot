
from aiogram import types
from aiogram.fsm.context import FSMContext
from app.globals import gigachat_api, database

# Обработчик для переписывания текста
async def rewrite_text_handler(message: types.Message, state: FSMContext):
    try:
        result = gigachat_api.rewrite_text(message.text)
        database.increment_user_requests(message.from_user.id)
        await message.answer(f"Вот переписанный текст:\n\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    database.update_user_state(message.from_user.id, None)
    await state.clear()

# Обработчик текста для анализа
async def analyze_text_handler(message: types.Message, state: FSMContext):
    try:
        result = gigachat_api.analyze_text(message.text)
        database.increment_user_requests(message.from_user.id)
        await message.answer(f"Результаты анализа текста:\n\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    database.update_user_state(message.from_user.id, None)
    await state.clear()

# Обработчик текста для рерайта
async def summarize_text_handler(message: types.Message, state: FSMContext):
    try:
        result = gigachat_api.summarize_text(message.text)
        database.increment_user_requests(message.from_user.id)
        await message.answer(f"Рерайт:\n\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    database.update_user_state(message.from_user.id, None)
    await state.clear()

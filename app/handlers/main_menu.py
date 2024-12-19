from aiogram import types
from aiogram.fsm.context import FSMContext
from app.globals import database, MainStates
from app.lexicon.lexicon import LEXICON


# Обработчик кнопок главного меню
async def handle_main_menu(message: types.Message, state: FSMContext):
    if message.text == "Переписать текст":
        await message.answer(LEXICON["rewrite_text"])
        database.update_user_state(message.from_user.id, "waiting_for_text_rewrite")
        await state.set_state(MainStates.waiting_for_text_rewrite)
    elif message.text == "Анализ текста":
        await message.answer(LEXICON["analyze_text"])
        database.update_user_state(message.from_user.id, "waiting_for_text_analysis")
        await state.set_state(MainStates.waiting_for_text_analysis)
    elif message.text == "Рерайт":
        await message.answer(LEXICON["summarize_text"])
        database.update_user_state(message.from_user.id, "waiting_for_text_summary")
        await state.set_state(MainStates.waiting_for_text_summary)
    elif message.text == "Показать статистику":
        stats = database.get_statistics(message.from_user.id)
        await message.answer(LEXICON["show_statistics"].format(stats=stats))
    else:
        await message.answer(LEXICON["invalid_option"])


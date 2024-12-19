from app.api.gigachat_api import GigaChatAPI
from aiogram.fsm.state import StatesGroup, State
from app.database.database import Database

# Конфигурация
GIGACHAT_API_KEY = "NjZhMTRlMjItMTU5OC00OGM2LThhMWQtODJiZDI4Nzk2MmYwOmIxN2Q0N2I3LTI4NjQtNDkzNi1iZmQyLTBmNTRjMjAxYzlmNw=="
DB_PATH = "C:/Users/User/PycharmProjects/gigiChat/app/db/text_rewriter.db"

# Состояния
class MainStates(StatesGroup):
    waiting_for_text_rewrite = State()
    waiting_for_text_analysis = State()
    waiting_for_text_summary = State()

# Глобальные объекты
gigachat_api = GigaChatAPI(api_key=GIGACHAT_API_KEY)
database = Database(db_path=DB_PATH)

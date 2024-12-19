
import sqlite3
import logging

class Database:
    def __init__(self, db_path="C:/Users/User/PycharmProjects/gigiChat/app/db/text_rewriter.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                state TEXT,
                requests_count INTEGER DEFAULT 0
            )
        ''')
        self.connection.commit()

    def add_user(self, user_id, username, state=None):
        self.cursor.execute('''
            INSERT OR IGNORE INTO users (user_id, username, state, requests_count)
            VALUES (?, ?, ?, 0)
        ''', (user_id, username, state))
        self.connection.commit()

    def update_user_state(self, user_id, state):
        self.cursor.execute('''
            UPDATE users SET state = ? WHERE user_id = ?
        ''', (state, user_id))
        self.connection.commit()

    def increment_user_requests(self, user_id):
        try:
            self.cursor.execute('''
                UPDATE users SET requests_count = requests_count + 1 WHERE user_id = ?
            ''', (user_id,))
            self.connection.commit()
        except Exception as e:
            logging.error(f"Ошибка при увеличении количества запросов: {e}")

    def get_statistics(self, user_id):
        try:
            self.cursor.execute('''
                SELECT requests_count FROM users WHERE user_id = ?
            ''', (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            logging.error(f"Ошибка при получении статистики: {e}")
            return 0

    def get_all_user_statistics(self):
        try:
            self.cursor.execute('''
                SELECT user_id, requests_count FROM users
            ''')
            results = self.cursor.fetchall()
            return [{"user_id": row[0], "requests_count": row[1]} for row in results]
        except Exception as e:
            logging.error(f"Ошибка при получении общей статистики: {e}")
            return []

    def close(self):
        self.connection.close()

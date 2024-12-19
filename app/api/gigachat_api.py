from gigachat import GigaChat

class GigaChatAPI:
    def __init__(self, api_key):
        self.gigachat = GigaChat(
            credentials=api_key,
            model="GigaChat",
            verify_ssl_certs=False,
            scope="GIGACHAT_API_PERS",
            streaming=False,
        )

    def rewrite_text(self, text):
        """
        Переписывает текст, сохраняя его смысл, но изменяя стиль и структуру.
        """
        context = "Перепиши текст, сохранив смысл, но изменив стиль и структуру."
        try:
            response = self.gigachat.chat(f"{context} {text}")
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise ValueError(f"Ошибка работы с GigaChat API: {e}")

    def analyze_text(self, text):
        """
        Проводит анализ текста и возвращает ключевые моменты.
        """
        context = "Проанализируй текст и выдели ключевые моменты."
        try:
            response = self.gigachat.chat(f"{context} {text}")
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise ValueError(f"Ошибка анализа текста через GigaChat API: {e}")

    def summarize_text(self, text):
        """
        Создает краткое изложение текста.
        """
        context = "Создай краткое изложение текста."
        try:
            response = self.gigachat.chat(f"{context} {text}")
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise ValueError(f"Ошибка создания резюме текста через GigaChat API: {e}")

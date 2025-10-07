## Telegram Resume Bot + FastAPI Skills API

Telegram-бот на **aiogram** и API на **FastAPI** для обработки резюме и извлечения ключевых навыков.

---

### Возможности

- `/resume` — принимает PDF или DOCX резюме, извлекает текст и отправляет его в API.  
- `/search` — выводит 3 заглушки вакансий с кнопками.  
- FastAPI-сервис `/extract_skills` — принимает текст и возвращает найденные навыки в формате JSON.

---

### Стек технологий

- Python 3.12  
- [aiogram 3.x](https://docs.aiogram.dev/en/latest/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- PyPDF2, python-docx — для извлечения текста  
- requests — для HTTP-запросов между ботом и API  

---

### Установка и запуск (локально)

1. Клонировать проект:
    ```bash
    git clone https://github.com/DimazKomarov/test_polza_agency.git
    cd test_polza_agency
    ```
2. Создать виртуальное окружение и установить зависимости:
    ```bash
    python -m venv venv
    source venv/bin/activate  # или venv\Scripts\activate на Windows
    pip install -r requirements.txt
    ```

3. Запустить API:
    ```bash
    uvicorn api:app --reload --port 8000
    ```

4. В другом терминале запустить бота:
    ```bash
    python bot.py
    ```
   
### Как работает

1. Пользователь отправляет боту файл .pdf или .docx.

2. Бот извлекает текст и отправляет его в FastAPI (/extract_skills).

3. API возвращает список навыков.

4. Бот выводит их пользователю.

### Пример ответа API
    POST /extract_skills

    ```json
    {
      "skills": ["python", "fastapi", "docker"]
    }
    ```


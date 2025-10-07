import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode
from docx import Document
from PyPDF2 import PdfReader
import io
import requests

API_TOKEN = "8182702063:AAGNRVaRc62_ZMeRpDLmAm_3emTIT5y6N74"
API_URL = "http://localhost:8000/extract_skills"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Используй /resume, чтобы загрузить резюме или /search для поиска вакансий.")


@dp.message(Command("resume"))
async def resume_prompt(message: types.Message):
    await message.answer("Пришлите файл резюме (PDF или DOCX).")


@dp.message(lambda msg: msg.document)
async def handle_resume(message: types.Message):
    file = await bot.get_file(message.document.file_id)
    file_bytes = await bot.download_file(file.file_path)
    content = file_bytes.read()

    text = ""
    if message.document.file_name.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = "\n".join(page.extract_text() for page in reader.pages)
    elif message.document.file_name.endswith(".docx"):
        doc = Document(io.BytesIO(content))
        text = "\n".join(p.text for p in doc.paragraphs)
    else:
        await message.answer("Поддерживаются только PDF и DOCX.")
        return

    await message.answer(f"Извлеченный текст:\n\n{text[:1500]}")

    # Отправляем текст в API для извлечения навыков
    try:
        response = requests.post(API_URL, json={"text": text})
        skills = response.json().get("skills", [])
        await message.answer(f"Ключевые навыки: {', '.join(skills)}")
    except Exception as e:
        await message.answer(f"Ошибка при обращении к API: {e}")


@dp.message(Command("search"))
async def search(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вакансия 1", url="https://example.com")],
        [InlineKeyboardButton(text="Вакансия 2", url="https://example.com")],
        [InlineKeyboardButton(text="Вакансия 3", url="https://example.com")]
    ])
    await message.answer("Вот 3 вакансии:", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

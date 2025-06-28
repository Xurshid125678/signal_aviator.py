import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = "7798824091:AAHDlgYIItVfx1O0ljykGO1q2qxB2VmRvFA"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# /start buyrug‘i handler (3.x versiyasiga mos)
@dp.message(F.text == "/start")
async def cmd_start(msg: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛒 Do‘konni ochish",
                web_app=WebAppInfo(
                    url="https://xurshidboyuzoqo-signalaviatorpy.your-repl.co/index.html"
                )
            )
        ]
    ])
    await msg.answer("Salom! Quyidagi tugmani bosib do‘konni oching:", reply_markup=kb)

# WebApp orqali yuborilgan ma’lumotni qabul qilish
@dp.message()
async def handle_webapp(msg: types.Message):
    if msg.web_app_data:
        await msg.answer(f"🛒 Savatga qo‘shildi: \n<code>{msg.web_app_data.data}</code>")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
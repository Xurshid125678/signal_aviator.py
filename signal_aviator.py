import telebot
import random

TOKEN = "7605231768:AAEtFHCuGaSpekfgdFVDcWtSa0czDdXAcmI"
bot = telebot.TeleBot(TOKEN)

# Signal variantlari
signals = [
    "🔥 Kuchli signal: 3.9x",
    "⚡ Blitz signal: 2.1x",
    "🎯 Oson signal: 1.6x",
    "💥 Tavakkal signal: 4.4x",
    "⬆️ Signal: 1.8x",
    "✈️ Signal: 2.3x"
]

# ID tekshiruv uchun saqlanadigan foydalanuvchilar ro'yxati
approved_users = set()

# /start komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    text = f"""👋 Salom, {name}!
Bu *Aviator signal boti* va u mutlaqo *TEKIN*! ✅

🎁 1Win promokodingiz orqali ro'yxatdan o'ting va 500 000 so'mgacha bonusga ega bo‘ling!

🔗 [1Win ro'yxatdan o'tish havolasi](https://1wxmeb.life/v3/reg-form-aviator?p=zm0k)

✅ Ro'yxatdan o'tgach, iltimos, o'z *1Win ID raqamingizni* shu yerga yuboring.
"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True)

# Foydalanuvchi ID yuborganda
@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_id(message):
    user_id = message.chat.id
    approved_users.add(user_id)

    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("🎰 Signal olish", callback_data="get_signal")
    markup.add(btn)

    bot.send_message(user_id, "✅ ID tasdiqlandi! Endi signal olishingiz mumkin 👇", reply_markup=markup)

# Signal tugmasi bosilganda
@bot.callback_query_handler(func=lambda call: call.data == "get_signal")
def send_signal(call):
    if call.message.chat.id not in approved_users:
        bot.send_message(call.message.chat.id, "❌ Avval ro'yxatdan o'ting va ID raqamingizni yuboring.")
        return

    signal = random.choice(signals)
    bot.send_message(call.message.chat.id, f"📡 {signal}\n🔁 Yana signal olish uchun tugmani bosing.")

print("✅ Bot ishga tushdi.")
bot.polling()
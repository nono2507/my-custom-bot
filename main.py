import os
import telebot

# جلب توكن البوت بأمان من إعدادات المنصة
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# رد تلقائي عند إرسال أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بكِ! أنا بوتكِ الخاص الذي قمتِ ببرمجته وتشغيله بنجاح تام ✨🤖")

# رد تلقائي على أي رسالة نصية أخرى
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أهلاً بكِ! لقد استقبلت رسالتكِ: {message.text}")

print("Bot is running successfully...")
bot.infinity_polling()

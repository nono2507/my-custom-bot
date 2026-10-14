import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot

# 1. خادم ويب مصغر لفتح البورت المطلوب من رندر (لجعله مجانياً 100%)
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    print(f"Web server running on port {port}")
    server.serve_forever()

# تشغيل خادم الويب في الخلفية لإرضاء منصة رندر
server_thread = threading.Thread(target=run_web_server)
server_thread.daemon = True
server_thread.start()

# 2. تشغيل بوت تيليجرام الخاص بكِ
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بكِ! أنا بوتكِ الخاص الذي قمتِ برمجته وتشغيله بنجاح تام وبدون أي تكلفة ✨🤖")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أهلاً بكِ! لقد استقبلت رسالتكِ: {message.text}")

print("Bot is running successfully...")
bot.infinity_polling()

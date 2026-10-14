import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot

# 1. خادم الويب المصغر للإبقاء على البوت مجانياً 24/7 على Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Streaming Bot is alive!")

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_web_server)
server_thread.daemon = True
server_thread.start()

# 2. إعدادات بوت تيليجرام الخاص بكِ
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بكِ في بوت البث الخاص بكِ! 🎬\nأرسلي لي أمر البث مع رابط يوتيوب وسأقوم بتجهيزه لكِ.")

@bot.message_handler(commands=['play'])
def play_media(message):
    # استخراج رابط يوتيوب أو الوسائط المرفقة من رسالة المستخدم
    query = message.text.replace('/play', '').strip()
    if not query:
        bot.reply_to(message, "الرجاء كتابة رابط يوتيوب بعد الأمر، مثال:\n`/play https://youtu.be/...`", parse_mode="Markdown")
        return
    
    bot.reply_to(message, f"⏳ جاري تجهيز البث للرابط:\n`{query}`\nقريباً سيتم ربطه بمشغل المحادثات الصوتية!", parse_mode="Markdown")

print("Streaming Bot is running...")
bot.infinity_polling()

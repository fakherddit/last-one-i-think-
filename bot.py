import telebot
import psycopg2
import random
from datetime import datetime, timedelta

# ================= CONFIGURATION =================
DB_URL = "postgresql://dylip_key_user:TwbqpTuAggFaAXhIX7Q7pMmJIih5vEQe@dpg-d5v88bl6ubrc73c8tlqg-a.oregon-postgres.render.com/dylip_key"
BOT_TOKEN = "8216359066:AAEt2GFGgTBp3hh_znnJagH3h1nN5A_XQf0"
ADMIN_ID = 7210704553
# =================================================

bot = telebot.TeleBot(BOT_TOKEN)

def get_db():
    conn = psycopg2.connect(DB_URL, sslmode='prefer')
    conn.autocommit = True
    return conn

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id != ADMIN_ID:
        return
    bot.reply_to(message, "Commands:\n/gen [days] [count] - Generate keys\n/global [days] - Generate global key\n/status - Server status\n/list - Last 10 keys")

@bot.message_handler(commands=['gen'])
def generate_key(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        parts = message.text.split()
        days = int(parts[1]) if len(parts) > 1 else 30
        count = int(parts[2]) if len(parts) > 2 else 1
        
        conn = get_db()
        cur = conn.cursor()
        
        generated = []
        for _ in range(count):
            key = "{:04X}-{:04X}-{:04X}-{:04X}".format(random.randint(0,0xFFFF), random.randint(0,0xFFFF), random.randint(0,0xFFFF), random.randint(0,0xFFFF))
            expiry = datetime.now() + timedelta(days=days)
            cur.execute("INSERT INTO licenses (license_key, expiry_date, key_type) VALUES (%s, %s, 'standard')", (key, expiry))
            generated.append(f"<code>{key}</code>")
        
        conn.close()
        bot.reply_to(message, f"Generated {count} keys ({days} days):\n" + "\n".join(generated), parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['list'])
def list_keys(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT license_key, expiry_date, hwid FROM licenses ORDER BY created_at DESC LIMIT 10")
        rows = cur.fetchall()
        conn.close()
        
        msg = "Last 10 Keys:\n"
        for r in rows:
            status = "🔴 Used" if r[2] else "🟢 New"
            msg += f"<code>{r[0]}</code> - {status}\n"
        bot.reply_to(message, msg, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

print("Bot is running...")
bot.infinity_polling()

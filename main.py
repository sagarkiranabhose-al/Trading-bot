import telebot
import random

TOKEN = "8782377003:AAGyLcEfX3QXyZdbbFS8HclavoJ0I91S4n4"

bot = telebot.TeleBot(TOKEN)

# ===== START COMMAND =====
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 
    "🚀 Welcome to SAGAR AI BOT\n\nCommands:\nNIFTY - Get Signal\nHELP - Help Menu")

# ===== HELP COMMAND =====
@bot.message_handler(func=lambda message: message.text.lower() == "help")
def help_msg(message):
    bot.reply_to(message,
    "📊 Commands:\n\nNIFTY - Live Signal\nHELLO - Test Bot")

# ===== NIFTY SIGNAL =====
@bot.message_handler(func=lambda message: message.text.lower() == "nifty")
def nifty_signal(message):
    signals = [
        "📈 BUY NIFTY 22800 CE\nSL: 22750\nTARGET: 22950",
        "📉 BUY NIFTY 22700 PE\nSL: 22780\nTARGET: 22600",
        "⚠️ SIDEWAYS MARKET - NO TRADE"
    ]
    bot.reply_to(message, random.choice(signals))

# ===== HELLO TEST =====
@bot.message_handler(func=lambda message: message.text.lower() == "hello")
def hello(message):
    bot.reply_to(message, "Hello Boss 😎 Bot Working!")

# ===== DEFAULT REPLY =====
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Type HELP for commands")

print("Bot Started...")
bot.polling()
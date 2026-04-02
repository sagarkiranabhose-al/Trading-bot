import time
import requests

# 🔹 Telegram Config
TELEGRAM_TOKEN = "8782377003:AAGyLcEfX3QXyZdbbFS8HclavoJ0I91S4n4"
CHAT_ID = "5586952772"  # Your Telegram ID

# 🔹 Function to send Telegram message
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

# 🔹 Bot Started
print("🚀 Trading Bot Started")
send_telegram("🚀 Trading Bot Started")  # Telegram notification

while True:
    # Dummy price (replace with real API later)
    price = 100

    if price > 90:
        signal = "BUY Signal ✅"
    else:
        signal = "SELL Signal ❌"

    print(signal)
    send_telegram(signal)  # Send signal to Telegram
    time.sleep(10)  # Delay between signals
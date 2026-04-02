import time

print("🚀 Trading Bot Started")

while True:
    print("Checking market...")
    
    # Dummy strategy (later real strategy add करेंगे)
    price = 100

    if price > 90:
        print("BUY Signal")
    else:
        print("SELL Signal")

    time.sleep(10)

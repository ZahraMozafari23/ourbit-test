import requests
import time
import os
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

DROP_PERCENT = 50
CHECK_INTERVAL = 300
alerted_coins = set()

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=data)


def get_market():

    url = "https://www.ourbit.com/api/platform/spot/market/v2/tickers"

    try:
        response = requests.get(url, timeout=10)
        print("STATUS:", response.status_code)
        print("TEXT:", response.text[:500])
        return response.json()

    except Exception as e:
        print("Market Error:", e)
        return None



def check_coins():

    data = get_market()

    if not data:
        return

    coins = data["data"]

    for coin in coins:

        symbol = coin["sb"]
        if symbol.startswith("~~"):
            continue
        
        change = float(coin["r8"]) * 100

        print(symbol, change)

        if change <= -50 and symbol not in alerted_coins:

            message = (
                "🚨 ریزش شدید ارز\n\n"
                f"🪙 ارز: {symbol}\n"
                f"📉 تغییر: {change:.2f}%"
            )

            send_message(message)

    
send_message("🚀 ربات هشدار Ourbit شروع شد")

while True:

    check_coins()

    time.sleep(CHECK_INTERVAL)

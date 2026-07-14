import requests

url = "https://www.ourbit.com/api/platform/spot/market/v2/tickers"

try:
    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    print("STATUS:", r.status_code)
    print(r.text[:500])

except Exception as e:
    print("ERROR:", e)

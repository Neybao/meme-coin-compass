import requests
import hmac
import hashlib
import time

def earn_locked(api_key, api_secret):
    base_url = "https://api.binance.com"
    endpoint = "/sapi/v1/simple-earn/flexible/position"
    timestamp = int(time.time() * 1000)

    query_string = f"timestamp={timestamp}"
    signature = hmac.new(api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    headers = {"X-MBX-APIKEY": api_key}
    url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

    response = requests.get(url, headers=headers)
    return response.json()

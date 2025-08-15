import requests

def get_price_history(coin_id="bitcoin", vs_currency="usd", days="30"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    response = requests.get(url, params=params)
    data = response.json()
    return data["prices"]


def get_coin_summary(coin_id="bitcoin", vs_currency="usd"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    params = {"localization": "false", "tickers": "false", "market_data": "true"}
    response = requests.get(url, params=params)
    data = response.json()
    market_data = data["market_data"]
    return {
        "name": data["name"],
        "symbol": data["symbol"].upper(),
        "price": market_data["current_price"][vs_currency],
        "volume": market_data["total_volume"][vs_currency],
        "market_cap": market_data["market_cap"][vs_currency],
        "change_24h": market_data["price_change_percentage_24h"]
    }

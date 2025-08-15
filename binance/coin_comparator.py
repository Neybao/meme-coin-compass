import pandas as pd

def compare_coins(coin1_data, coin2_data):
    df = pd.DataFrame([coin1_data, coin2_data])
    df.set_index("symbol", inplace=True)
    return df

def get_coin_summary(coin_id):
    import requests
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "symbol": coin_id,
            "price": data["market_data"]["current_price"]["brl"],
            "volume": data["market_data"]["total_volume"]["brl"],
            "market_cap": data["market_data"]["market_cap"]["brl"],
            "change_24h": data["market_data"]["price_change_percentage_24h"]
        }
    return None

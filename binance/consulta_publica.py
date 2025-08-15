import requests

def obter_dados_mercado(symbol: str) -> dict:
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "price": float(data["lastPrice"]),
            "volume": float(data["quoteVolume"]),
            "change_24h": float(data["priceChangePercent"])
        }
    except Exception as e:
        print(f"Erro ao consultar dados de mercado: {e}")
        return None

def obter_historico(symbol: str, intervalo: str = "1h", limite: int = 24):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={intervalo}&limit={limite}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [float(item[4]) for item in data]  # Preço de fechamento
    except Exception as e:
        print(f"Erro ao obter histórico: {e}")
        return []

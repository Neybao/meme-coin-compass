import requests

def consultar_binance_publico(simbolo):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Erro ao consultar Binance: {e}")
        return None



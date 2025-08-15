import requests

def converter_fiat(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"][para]
    except:
        return None

def converter_crypto(valor, crypto_id, moeda_destino):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={moeda_destino}"
    try:
        response = requests.get(url)
        data = response.json()
        return valor * data[crypto_id][moeda_destino]
    except:
        return None
def converter_moeda(valor, origem, destino):
    fiat = ["BRL", "USD", "EUR"]
    if origem in fiat and destino in fiat:
        return converter_fiat(valor, origem, destino)
    else:
        return converter_crypto(valor, origem, destino)

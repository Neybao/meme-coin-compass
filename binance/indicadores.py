from pycoingecko import CoinGeckoAPI
import pandas as pd
import talib

cg = CoinGeckoAPI()

def obter_dados_historicos(moeda_id, dias=30):
    dados = cg.get_coin_market_chart_by_id(id=moeda_id, vs_currency='usd', days=dias)
    df = pd.DataFrame(dados['prices'], columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('date', inplace=True)
    return df

def calcular_macd(df):
    macd, macd_signal, macd_hist = talib.MACD(df['price'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    df['macd'] = macd
    df['macd_signal'] = macd_signal
    df['macd_hist'] = macd_hist
    return df

def calcular_rsi(df):
    df['rsi'] = talib.RSI(df['price'].values, timeperiod=14)
    return df



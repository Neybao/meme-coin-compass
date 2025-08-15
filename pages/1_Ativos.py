import streamlit as st
from binance.conexao import consultar_binance_publico

st.set_page_config(page_title="💼 Ativos Públicos", layout="wide")
st.title("💼 Preços de Ativos (dados públicos)")

ativos = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "DOGEUSDT"]
valores = {}

for simbolo in ativos:
    dados = consultar_binance_publico(simbolo)
    if dados:
        valores[simbolo] = float(dados["price"])

cols = st.columns(len(valores))
for i, (moeda, preco) in enumerate(valores.items()):
    cols[i].metric(label=moeda, value=f"${preco:.2f}")



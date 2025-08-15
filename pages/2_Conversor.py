import streamlit as st
from binance.conexao import consultar_binance_publico

st.set_page_config(page_title="💱 Conversor de Moedas", layout="wide")
st.title("💱 Conversor de Moedas (dados públicos)")

moeda_origem = st.selectbox("Moeda de origem", ["BTC", "ETH", "BNB", "SOL", "DOGE"])
moeda_destino = st.selectbox("Moeda de destino", ["USDT", "BRL"])
quantidade = st.number_input("Quantidade a converter", min_value=0.0, format="%.6f")

simbolo = f"{moeda_origem}{moeda_destino}"
dados = consultar_binance_publico(simbolo)

if dados and quantidade > 0:
    preco = float(dados["price"])
    convertido = quantidade * preco
    st.metric(label=f"{moeda_origem} ➡ {moeda_destino}", value=f"{convertido:.2f}", delta=f"1 {moeda_origem} = {preco:.2f} {moeda_destino}")


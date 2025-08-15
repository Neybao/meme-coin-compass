import streamlit as st
from binance.conexao import consultar_binance_publico
import plotly.graph_objects as go

st.set_page_config(page_title="⚖️ Comparador de Ativos", layout="wide")
st.title("⚖️ Comparador de Ativos (dados públicos)")

ativos = st.multiselect("Escolha até 3 ativos", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"], default=["BTCUSDT", "ETHUSDT"])

valores = {}
for simbolo in ativos:
    dados = consultar_binance_publico(simbolo)
    if dados:
        valores[simbolo] = float(dados["price"])

fig = go.Figure()
for ativo, preco in valores.items():
    fig.add_trace(go.Bar(name=ativo, x=[ativo], y=[preco]))

fig.update_layout(title="📈 Preços Atuais", yaxis_title="Preço (USDT)")
st.plotly_chart(fig, use_container_width=True)


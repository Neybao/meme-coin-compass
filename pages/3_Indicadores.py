import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="📊 Indicadores Técnicos", layout="wide")
st.title("📊 Indicadores Técnicos (simulados)")

ativo = st.selectbox("Escolha o ativo", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"])

# Simulação de RSI
rsi = [30, 45, 60, 70]
datas_rsi = ["Dia 1", "Dia 2", "Dia 3", "Dia 4"]

fig_rsi = go.Figure()
fig_rsi.add_trace(go.Scatter(x=datas_rsi, y=rsi, mode="lines", name="RSI"))
fig_rsi.update_layout(yaxis_range=[0, 100], title="RSI Simulado")
st.plotly_chart(fig_rsi, use_container_width=True)

# Simulação de MACD
macd = [1.2, 1.5, 1.3]
signal = [1.0, 1.2, 1.1]
datas_macd = ["Dia 1", "Dia 2", "Dia 3"]

fig_macd = go.Figure()
fig_macd.add_trace(go.Scatter(x=datas_macd, y=macd, mode="lines", name="MACD"))
fig_macd.add_trace(go.Scatter(x=datas_macd, y=signal, mode="lines", name="Signal"))
fig_macd.update_layout(title="MACD Simulado")
st.plotly_chart(fig_macd, use_container_width=True)


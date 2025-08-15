import streamlit as st
import time
import plotly.graph_objects as go
from binance.consulta_publica import obter_dados_mercado, obter_historico

# Verificação de login
#if "usuario_logado" not in st.session_state or st.session_state.usuario_logado is None:
 #   st.warning("🔒 Você precisa estar logado para acessar esta página.")
  #  st.stop()

st.set_page_config(page_title="Consulta Pública", layout="wide")
st.title("🌐 Consulta Pública da Binance")

# Escolha da moeda
moeda = st.selectbox("Escolha uma moeda", ["BTCUSDT", "ETHUSDT", "SOLUSDT", "ADAUSDT", "DOGEUSDT"])

# Atualização automática
col1, col2 = st.columns([1, 3])
with col1:
    atualizar = st.checkbox("🔄 Atualizar automaticamente")
with col2:
    intervalo = st.slider("Intervalo (segundos)", 5, 60, 10)

if atualizar:
    time.sleep(intervalo)
    st.experimental_rerun()

# Dados de mercado
dados = obter_dados_mercado(moeda)

if dados:
    st.metric("💰 Preço Atual", f"${dados['price']:.2f}")
    st.metric("📊 Volume 24h", f"${dados['volume']:.0f}")
    st.metric("📈 Variação 24h", f"{dados['change_24h']:.2f}%")

    # Alerta personalizado
    preco_alvo = st.number_input("🔔 Me avise se o preço cair abaixo de:", min_value=0.0, value=100000.0)
    if dados["price"] < preco_alvo:
        st.error(f"🚨 Alerta: o preço atual de {moeda} caiu para ${dados['price']:.2f}, abaixo do seu alvo de ${preco_alvo:.2f}!")

    # Gráfico de histórico
    historico = obter_historico(moeda)
    if historico:
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=historico, mode="lines", name="Preço"))
        fig.update_layout(title="📉 Histórico de Preço (últimas 24h)", xaxis_title="Horas", yaxis_title="Preço")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Não foi possível carregar o histórico de preços.")
else:
    st.warning("Não foi possível obter os dados da moeda selecionada.")

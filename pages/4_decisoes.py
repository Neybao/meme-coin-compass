import streamlit as st
import plotly.graph_objects as go
from binance.consulta_publica import obter_dados_mercado, obter_historico

st.set_page_config(page_title="🧠 Decisões Estratégicas", layout="wide")
st.title("🧠 Decisões Estratégicas com Base em Indicadores")

# Escolha da moeda
moeda = st.selectbox("Ativo para análise", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"])

# Obter dados públicos
dados = obter_dados_mercado(moeda)
historico = obter_historico(moeda)

if dados and historico:
    # Cálculo de média móvel simples (últimas 24h)
    if "price" in dados:
        preco_atual = dados["price"]
    else:
        st.warning("Não foi possível obter o preço atual para análise.")
        st.stop()

    if historico:
        media_24h = sum(historico) / len(historico)
    else:
        st.warning("Não foi possível obter o histórico para análise.")
        st.stop()

    delta = preco_atual - media_24h
    forca = f"{(delta / media_24h) * 100:.2f}%"

    if delta > 0:
        tendencia = "Alta"
        texto = "📈 A tendência atual é de alta com base na média das últimas 24h."
    elif delta < 0:
        tendencia = "Baixa"
        texto = "📉 A tendência atual é de baixa com base na média das últimas 24h."
    else:
        tendencia = "Estável"
        texto = "🔄 O preço está estável em relação à média das últimas 24h."

    # Exibir recomendação
    st.subheader("📌 Recomendação Estratégica")
    st.success(texto)
    st.metric(label="Tendência", value=tendencia, delta=forca)

    # Exibir gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=historico, mode="lines", name="Preço"))
    fig.update_layout(title="📉 Histórico de Preço (últimas 24h)", xaxis_title="Horas", yaxis_title="Preço")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Não foi possível obter os dados para análise.")


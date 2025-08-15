import streamlit as st

st.set_page_config(page_title="📬 Alertas e Sugestões", layout="wide")
st.title("📬 Alertas e Sugestões (simulados)")

alertas = [
    {"mensagem": "RSI acima de 70 em BTC", "ativo": "BTC", "nivel": "Alto", "acao": "Vender"},
    {"mensagem": "MACD cruzando linha de sinal em ETH", "ativo": "ETH", "nivel": "Médio", "acao": "Observar"}
]

for alerta in alertas:
    st.warning(f"🚨 {alerta['mensagem']}")
    st.write(f"Ativo: {alerta['ativo']} | Nível: {alerta['nivel']} | Ação sugerida: **{alerta['acao']}**")


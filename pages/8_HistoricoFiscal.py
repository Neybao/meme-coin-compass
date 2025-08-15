import streamlit as st
from binance.transacoes import obter_historico_transacoes
import pandas as pd

if "usuario_logado" not in st.session_state or st.session_state.usuario_logado is None:
    st.warning("🔒 Você precisa estar logado para acessar esta página.")
    st.stop()

st.set_page_config(page_title="🧾 Histórico Fiscal", layout="wide")
st.title("🧾 Histórico de Transações e Impostos")

api_key = st.text_input("API Key")
api_secret = st.text_input("API Secret", type="password")

if api_key and api_secret:
    transacoes = obter_historico_transacoes(api_key, api_secret)

    if transacoes:
        df = pd.DataFrame(transacoes)
        st.dataframe(df)

        total_ganho = df[df["tipo"] == "venda"]["lucro"].sum()
        st.metric(label="Lucro Total", value=f"R$ {total_ganho:.2f}")
    else:
        st.info("Nenhuma transação fiscal encontrada.")

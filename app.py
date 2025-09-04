from pathlib import Path
import streamlit as st
from PIL import Image
import os
import requests

# Caminho absoluto usando pathlib
banner_path = Path(__file__).parent / "login_banner.png"

# Configuração da página
st.set_page_config(page_title="MemeCoin Compass", layout="centered")

# Tema visual tricolor 🔴⚪⚫
st.markdown("""
<style>
body, .main {
    background-color: #0F0F0F;
    color: #FFFFFF;
}
h1, h2, h3 {
    color: #FF0000;
}
button {
    background-color: #FF0000;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: bold;
}
input {
    background-color: #1C1C1C;
    color: white;
    border: 1px solid #FF0000;
    border-radius: 6px;
}
[data-testid="stSidebar"] {
    background-color: #181818;
    color: white;
}
hr {
    border-top: 1px solid #FF0000;
}
a {
    color: #FF0000;
}
</style>
""", unsafe_allow_html=True)

# Caminho do banner
#banner_path = "login_banner.png"

# Função para exibir o banner

def exibir_banner(pagina, tema):
    banners = {
        "home": {
            "claro": "https://i.postimg.cc/Hj6HZGn/Copilot-20250815-074805.png",
            "escuro": "https://i.postimg.cc/xyz123/banner-home-escuro.png"
        },
        "login": {
            "claro": "https://i.postimg.cc/abc456/banner-login-claro.png",
            "escuro": "https://i.postimg.cc/def789/banner-login-escuro.png"
        }
    }
    url_banner = banners.get(pagina, {}).get(tema)
    if url_banner:
        st.image(url_banner, use_container_width=True)

# Inicializa variáveis de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
if "usuarios" not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

# Função de login
def login():
    usuario = st.session_state["usuario"]
    senha = st.session_state["senha"]
    if st.session_state.usuarios.get(usuario) == senha:
        st.session_state.logado = True
        st.success("✅ Login realizado com sucesso!")
        st.experimental_rerun()
    else:
        st.error("❌ Usuário ou senha inválidos.")

# Função de cadastro
def cadastrar():
    novo_usuario = st.session_state["novo_usuario"]
    nova_senha = st.session_state["nova_senha"]
    if novo_usuario in st.session_state.usuarios:
        st.warning("⚠️ Usuário já existe.")
    else:
        st.session_state.usuarios[novo_usuario] = nova_senha
        st.success("✅ Cadastro realizado com sucesso!")

# Interface de login
if not st.session_state.logado:
    exibir_banner("login", "claro")
    st.markdown("## 🔐 Acesse sua conta")
    st.text_input("🧑 Usuário", key="usuario")
    st.text_input("🔒 Senha", type="password", key="senha")
    st.button("Entrar", on_click=login)

    st.markdown("---")
    st.markdown("### Ainda não tem conta?")
    st.text_input("🆕 Novo usuário", key="novo_usuario")
    st.text_input("🔑 Nova senha", type="password", key="nova_senha")
    st.button("Cadastrar", on_click=cadastrar)

# Interface principal após login
else:
    st.sidebar.success("✅ Você está logado!")
    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.experimental_rerun()

    # Menu lateral com ícones
    menu = st.sidebar.radio("📌 Navegação", [
        "💼 Meus Ativos", "💱 Conversor", "📊 Indicadores", "📘 Decisões",
        "🔍 Comparador", "📈 Recomendações", "📡 Consulta Pública", "📋 Histórico Fiscal"
    ])

    # Conteúdo das páginas
    if menu == "💼 Meus Ativos":
        st.title("💼 Meus Ativos")
        ativos = {"bitcoin": 0.5, "ethereum": 2.1, "solana": 10, "usd-coin": 1000, "dogecoin": 5000}
        ids = ','.join(ativos.keys())
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={ids}'
        try:
            r = requests.get(url, timeout=10)
            data = r.json()
            for coin in data:
                col1, col2 = st.columns([1,6])
                with col1:
                    st.image(coin['image'], width=40)
                with col2:
                    st.markdown(f"**{coin['symbol'].upper()}** — {coin['name']}")
                    st.markdown(f"Saldo: `{ativos[coin['id']]:,.4f}` | Cotação: `${coin['current_price']:,.2f}`")
        except Exception as e:
            st.error(f"Erro ao buscar dados da CoinGecko: {e}")

    elif menu == "💱 Conversor":
        st.title("💱 Conversor Inteligente")
        moedas = ["BRL", "USD", "EUR", "BTC", "ETH"]
        moeda_origem = st.selectbox("Moeda de origem", moedas, key="moeda_origem")
        moeda_destino = st.selectbox("Moeda de destino", moedas, key="moeda_destino")
        valor = st.number_input("Valor a converter", min_value=0.0, format="%.4f", key="valor_converter")
        taxas = {
            ("BRL", "USD"): 0.20, ("USD", "BRL"): 5.00,
            ("BRL", "EUR"): 0.18, ("EUR", "BRL"): 5.50,
            ("USD", "EUR"): 0.90, ("EUR", "USD"): 1.10,
            ("BTC", "USD"): 60000, ("USD", "BTC"): 1/60000,
            ("ETH", "USD"): 3500, ("USD", "ETH"): 1/3500,
        }
        if st.button("Converter", key="botao_converter_moeda"):
            if moeda_origem == moeda_destino:
                st.info("Selecione moedas diferentes para converter.")
            else:
                taxa = taxas.get((moeda_origem, moeda_destino))
                if taxa:
                    resultado = valor * taxa
                    st.success(f"{valor:.4f} {moeda_origem} = {resultado:.4f} {moeda_destino}")
                else:
                    st.warning("Conversão não suportada nesta simulação.")

    elif menu == "📊 Indicadores":
        st.title("📊 Indicadores Técnicos")
        st.info("Funcionalidade de indicadores técnicos aqui.")

    elif menu == "📘 Decisões":
        st.title("📘 Histórico de Decisões")
        st.info("Funcionalidade de decisões aqui.")

    elif menu == "🔍 Comparador":
        st.title("🔍 Comparador de Moedas")
        st.info("Funcionalidade de comparação de moedas aqui.")

    elif menu == "📈 Recomendações":
        st.title("📈 Recomendação de Mercado")
        st.info("Funcionalidade de recomendações aqui.")

    elif menu == "📡 Consulta Pública":
        st.title("📡 Consulta Pública Binance")
        st.info("Funcionalidade de consulta pública aqui.")

    elif menu == "📋 Histórico Fiscal":
        st.title("📋 Histórico de Consultas Fiscais")
        st.info("Funcionalidade de histórico fiscal aqui.")

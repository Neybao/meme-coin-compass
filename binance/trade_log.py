import pandas as pd
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "historico_decisoes.csv")

def registrar_decisao(usuario, moeda, acao, motivo, preco):
    nova_linha = {
        "Usuário": usuario,
        "Moeda": moeda,
        "Ação": acao,
        "Motivo": motivo,
        "Preço": preco,
        "Data": pd.Timestamp.now()
    }

    if os.path.exists(LOG_PATH):
        df = pd.read_csv(LOG_PATH)
        df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
    else:
        df = pd.DataFrame([nova_linha])

    df.to_csv(LOG_PATH, index=False)

def carregar_historico():
    if os.path.exists(LOG_PATH):
        return pd.read_csv(LOG_PATH)
    else:
        return pd.DataFrame(columns=["Usuário", "Moeda", "Ação", "Motivo", "Preço", "Data"])

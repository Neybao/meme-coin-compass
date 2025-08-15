import requests
import re
import pandas as pd
import os
from datetime import datetime  # [Nova linha 5]
# 🔑 Chave da API fiscal
API_KEY_FISCAL = "essaQrSmOnaU0Dx0OhFEhV5CH1faGKJqOcje0Cg2kWDXq4cmRp0gP8nDr64QMLIjr1Z"

def validar_cnpj(cnpj):
    """
    Valida se o CNPJ possui 14 dígitos numéricos.
    """
    return bool(re.fullmatch(r"\d{14}", cnpj))

def salvar_consulta_csv(dados):
    """
    Salva os dados da consulta fiscal em um arquivo CSV, evitando duplicatas por CNPJ.
    Organiza colunas e inclui data da consulta.
    """
    caminho = "consultas_fiscais.csv"

    # Campos desejados para visualização
    campos_desejados = [
        "cnpj", "nome", "fantasia", "telefone",
        "email", "municipio", "uf", "situacao"
    ]

    # Filtra os campos e adiciona data
    dados_filtrados = {campo: dados.get(campo, "") for campo in campos_desejados}
    dados_filtrados["data_consulta"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    novo_df = pd.DataFrame([dados_filtrados])
    cnpj_novo = dados_filtrados["cnpj"]

    if os.path.exists(caminho):
        df_antigo = pd.read_csv(caminho)

        # Verifica se o CNPJ já foi consultado
        if cnpj_novo in df_antigo["cnpj"].values:
            return  # Evita duplicata

        df_final = pd.concat([df_antigo, novo_df], ignore_index=True)
    else:
        df_final = novo_df

    df_final.to_csv(caminho, index=False)


def consultar_cnpj(cnpj, chave_recebida):
    """
    Consulta informações de um CNPJ na API da ReceitaWS.
    """
    if chave_recebida != API_KEY_FISCAL:
        return {"erro": "Chave inválida"}

    if not validar_cnpj(cnpj):
        return {"erro": "CNPJ inválido. Use apenas números (14 dígitos)."}

    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            salvar_consulta_csv(dados)  # Salva os dados após consulta bem-sucedida
            return dados
        else:
            return {"erro": f"Erro na consulta: {resposta.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"erro": f"Falha na requisição: {str(e)}"}

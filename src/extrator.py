from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
def extrair_valores():
    linha = 0
    coluna = 0
    PLANILHA = os.getenv("CNPJ")

    dados_planilha = pd.read_excel(PLANILHA, usecols=[coluna], skiprows=linha, sheet_name=0, header=None, dtype=str)
    print(f'Dados da planilha:\n{dados_planilha}')
    valores_coluna = dados_planilha[coluna].tolist()

    return valores_coluna
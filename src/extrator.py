from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
def extrair_valores():
    linha = 0
    coluna = 0
    PLANILHA = os.getenv("CNPJ")

    try:
        dados_planilha = pd.read_excel(PLANILHA, usecols=[coluna], skiprows=linha, sheet_name=0, header=None, dtype=str)
        print(
            "="*20 +
            f"\nDados da planilha:\n{dados_planilha}\n" +
            "="*20 +
            "\n"
        )
        valores_coluna = dados_planilha[coluna].tolist()

    except Exception as e:
        print(f'Erro ao extrair dados da planilha: {e}')
        valores_coluna = []

    return valores_coluna
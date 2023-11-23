import time
import requests
import pandas as pd
import numpy as np
from openpyxl import Workbook

planilha_cnpj = "nova.xlsx"

coluna = 0
dados_planilha = pd.read_excel("nova.xlsx", usecols=[coluna], header=None)
valores_coluna = dados_planilha[coluna].tolist()

array_coluna_cnpj = np.array(valores_coluna)

"""=========================================================================================="""

def obter_informacoes_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados_empresa = response.json()
        
        print(f'\n{dados_empresa}\n')

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')

"""=========================================================================================="""    
#Dados excel CNPJs
cnpj_exemplo = array_coluna_cnpj
#API
response = requests.get("https://receitaws.com.br/v1/cnpj/{cnpj}")
"""index = 0
lista_cnpj = []

while index <= 1: 
    obter_informacoes_cnpj(cnpj_exemplo[index])
    print("Requisição bem-sucedida!")
    print("Aguarde...\n")
    time.sleep(2)
    index += 1
"""
"""==========================================================================================""" 

# Dados acumulados da API
dados_acumulados = []

# Consulta API e acumula os dados
for cnpj_exemplo in array_coluna_cnpj:
    dados_empresa = obter_informacoes_cnpj(cnpj_exemplo)
    
    #Verifica se está pegando algum dado de 'dados_empresa'
    print(dados_empresa)
    print("Consultando próximo CNPJ...")
    time.sleep(3)

    if dados_empresa:
        dados_acumulados.append(dados_empresa)
        time.sleep(1)

    if cnpj_exemplo == '':
        print("Nenhum CNPJ encontrado!")

# Criar DataFrame pandas com os dados acumulados
df_acumulado = pd.DataFrame(dados_acumulados)

# Salvar DataFrame no Excel
with pd.ExcelWriter('dados_acumulados.xlsx', engine='openpyxl') as writer:
    print(dados_acumulados)
    df_acumulado.to_excel(writer, sheet_name='Sheet1', index=False)
    print("Planilha atualizada!")
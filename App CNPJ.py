# -*- coding: utf-8 -*-

import time
import json
import requests
import pandas as pd
import numpy as np
import threading

# Manipulação da planilha

planilha_cnpj = "CNPJs.xlsx"
coluna = 1
linha = 1

dados_planilha = pd.read_excel(planilha_cnpj, usecols=[coluna], skiprows=linha, sheet_name='CNPJs', header=None, dtype=str)
print(dados_planilha)
valores_coluna = dados_planilha[coluna].tolist()
print(valores_coluna)

array_coluna_cnpj = np.array(valores_coluna)

"""=========================================================================================="""

# API
def obter_informacoes_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados_empresa = response.json()
        resp = json.loads(response.text)
        return dados_empresa
        print(resp['nome'])

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')

"""=========================================================================================="""   

# Dados do excel (CNPJs)
cnpj_exemplo = array_coluna_cnpj

"""==========================================================================================""" 

# Inicialização
dados_acumulados = []
cont = 0

print("\nIniciando...\n")
time.sleep(3)

# Função para a contagem regressiva
def contador(tempo_total):
    while tempo_total > 0:
        print(f"Tempo para a próxima consulta: {tempo_total} segundos", end='\r')
        time.sleep(1)
        tempo_total -= 1

# Consulta API e acumula os dados
for cnpj_exemplo in array_coluna_cnpj:

    if cont == 3:
        print("A aplicação consulta apenas 3 CNPJs por minuto, por favor, aguarde...")
        print(f"CNPJs consultados: {len(dados_acumulados)}")
        print(f"CNPJs faltantes: {(len(array_coluna_cnpj)) - (len(dados_acumulados))}\n")

        thread_contador = threading.Thread(target=contador, args=(60,))
        thread_contador.start()

        time.sleep(60)
        thread_contador.join()

        cont = 0
    
    dados_empresa = obter_informacoes_cnpj(cnpj_exemplo)

    if dados_empresa:
        print(f"\nConsultando o CNPJ: {cnpj_exemplo}\n")
        dados_acumulados.append(dados_empresa)
        time.sleep(2)
        
    cont += 1

"""==========================================================================================""" 

# Criar DataFrame com os dados acumulados
df_acumulado = pd.DataFrame(dados_acumulados)

# Salvar DataFrame no Excel
with pd.ExcelWriter('Planilha de CNPJs.xlsx', engine='openpyxl') as writer:
    print(f"\nTotal de consultas: {len(dados_acumulados)}")

    df_acumulado.to_excel(writer, sheet_name='CNPJs', index=False)
    print("\nPlanilha de CNPJs criada com sucesso!\n")

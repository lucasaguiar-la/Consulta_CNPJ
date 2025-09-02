
import json
import requests

def obter_informacoes_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados_empresa = response.json()
        resp = json.loads(response.text)
        print(resp['nome'])
        return dados_empresa

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
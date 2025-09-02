
import json
import requests

def buscar_infos(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        req = requests.get(url)
        req.raise_for_status()

        dados_empresa = req.json()
        print(dados_empresa)

        resp = json.loads(req.text)
        print(resp['nome'])

        return dados_empresa

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
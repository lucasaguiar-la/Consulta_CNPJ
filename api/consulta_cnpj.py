from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()
def buscar_infos(cnpj):
    url = os.getenv("API") + cnpj

    try:
        req = requests.get(url)
        req.raise_for_status()
        dados_empresa = req.json()

        resp = json.loads(req.text)
        print(
            "\nConsultando...\n"
            f"CNPJ: {resp['cnpj']}\n"
            f"Nome Empresa: {resp['nome']}\n"
        )

        return dados_empresa

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
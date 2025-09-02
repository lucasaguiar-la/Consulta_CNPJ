# -*- coding: utf-8 -*-

from src.inicia_app import executa_app
from src.salva_planilha import salvar_planilha
from time import sleep

if __name__ == "__main__":
    print("\nIniciando...\n")
    sleep(1)
    dados = executa_app()

    if dados:
        print("Salvando dados consultados...")
        salvar_planilha(dados)

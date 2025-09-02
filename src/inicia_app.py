from api.consulta_cnpj import buscar_infos
from src.extrai_dados import extrair_valores
from src.utils import contador
from time import sleep
import threading

def executa_app():
    cont = 0
    dados_acumulados = []
    lista_cnpj = extrair_valores()

    for cnpj in lista_cnpj:

        if cont == 3:
            print(
                "\nA aplicação consulta (gratuitamente) apenas 3 CNPJs por minuto, por favor, aguarde...\n",
                f"CNPJs consultados: {len(dados_acumulados)}\n",
                f"CNPJs faltantes: {(len(lista_cnpj)) - (len(dados_acumulados))}\n"
            )

            thread_contador = threading.Thread(target=contador, args=(60,))
            thread_contador.start()

            sleep(61)
            thread_contador.join()

            cont = 0

        try:
            dados_empresa = buscar_infos(cnpj)

            if dados_empresa:
                dados_acumulados.append(dados_empresa)
                sleep(2)
                
            cont += 1
        
        except Exception as e:
            print(f'Erro ao consultar o CNPJ {cnpj}: {e}')
    
    return dados_acumulados

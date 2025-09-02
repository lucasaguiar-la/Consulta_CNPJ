import time

def contador(tempo_total):
    while tempo_total > 0:
        print(f"Tempo para a próxima consulta: {tempo_total} segundos", end='\r')
        time.sleep(1)
        tempo_total -= 1
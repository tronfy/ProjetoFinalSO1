from random import randint
from threading import Thread
from time import sleep

from Encomenda import Encomenda
from Ponto import Ponto
from Veiculo import Veiculo


S = 5
C = 3
P = 10
A = 5

encomendas: list[Encomenda] = []
pontos: list[Ponto] = []
veiculos: list[Veiculo] = []

# criar encomendas
for i in range(P):
    origem = randint(0, S - 1)
    while True:
        destino = randint(0, S - 1)
        if destino != origem:
            break

    encomendas.append(Encomenda(i, origem, destino))

# criar veículos
for i in range(C):
    id_ponto_inicial = randint(0, S - 1)
    veiculos.append(Veiculo(i, id_ponto_inicial, A, S))

# criar pontos
for i in range(S):
    encomendas_ponto = [e for e in encomendas if e.id_ponto_origem == i]
    pontos.append(Ponto(i, encomendas_ponto, veiculos))

# iniciar threads
for veiculo in veiculos:
    veiculo.thread.start()
for ponto in pontos:
    ponto.thread.start()
# for encomenda in encomendas:
#     encomenda.thread.start()


# def verifica_fim():
#     while True:
#         end = True

#         for ponto in pontos:
#             if len(ponto.fila_encomendas) > 0:
#                 end = False
#                 break

#         for veiculo in veiculos:
#             if len(veiculo.encomendas) > 0:
#                 end = False
#                 break

#         if end:
#             # mata todas as threads e encerra o programa
#             for veiculo in veiculos:
#                 veiculo.thread._stop()
#             for ponto in pontos:
#                 ponto.thread._stop()
#             # for encomenda in encomendas:
#             #     encomenda.thread._stop()

#         sleep(1)


# fim_thread = Thread(target=verifica_fim)
# fim_thread.start()
# fim_thread.join()


# join threads
for veiculo in veiculos:
    veiculo.thread.join()
for ponto in pontos:
    ponto.thread.join()
# for encomenda in encomendas:
#     encomenda.thread.join()

# loop que checa por condição de parada:
# todo ponto.fila_encomendas vazia
# todo veiculo.encomendas vazia

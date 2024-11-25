import sys
import os
from random import randint
from threading import Thread
from time import sleep

from Encomenda import Encomenda
from Monitoramento import log, monitorar
from Ponto import Ponto
from Veiculo import Veiculo


if len(sys.argv) < 5:
    print("use: main.py S C P A")
    sys.exit(1)

S = int(sys.argv[1])
C = int(sys.argv[2])
P = int(sys.argv[3])
A = int(sys.argv[4])

if P <= A or A <= C:
    print("argumentos violam regra: P >> A >> C")
    sys.exit(1)

encomendas: list[Encomenda] = []
pontos: list[Ponto] = []
veiculos: list[Veiculo] = []


if not os.path.exists("encomendas"):
    os.makedirs("encomendas")

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
monitoramento = Thread(target=monitorar, args=(pontos, veiculos, encomendas))
monitoramento.start()

for veiculo in veiculos:
    veiculo.thread.start()
for ponto in pontos:
    ponto.thread.start()
for encomenda in encomendas:
    encomenda.thread.start()

# encomendas finalizam suas threads quando são entregues
for encomenda in encomendas:
    encomenda.thread.join()

log("TODAS as ENCOMENDAS foram entregues")

# veículos finalizam suas threads quando derem uma volta completa sem coletar ou entregar encomendas
for veiculo in veiculos:
    veiculo.thread.join()

log("TODOS os VEÍCULOS deram uma volta completa sem coletar ou entregar encomendas")

for ponto in pontos:
    ponto.finalizar()
    # ponto.thread.join()

log("TODOS os PONTOS foram finalizados")

monitoramento.join()

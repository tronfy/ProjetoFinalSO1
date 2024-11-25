from __future__ import annotations
from typing import TYPE_CHECKING

from monitoramento import log

if TYPE_CHECKING:
    from Encomenda import Encomenda

from random import randint
from time import sleep
from threading import Semaphore, Thread


class Veiculo:
    def __init__(self, id: int, id_ponto_atual: int, A: int, S: int):
        self.id = id
        self.id_ponto_atual: int = id_ponto_atual
        self.encomendas: list[Encomenda] = []
        self.A = A  # número máximo de encomendas que o veículo pode carregar
        self.S = S  # número de pontos de distribuição

        self.semaphore = Semaphore(0)
        self.em_transito = False
        self.visitas_sem_encomenda = 0

        self.thread = Thread(target=self.loop)

    def descarrega_encomendas(self) -> list[Encomenda]:
        descarregando = []

        # selecionar encomedas a descarregar
        for encomenda in self.encomendas:
            if encomenda.id_ponto_destino == self.id_ponto_atual:
                descarregando.append(encomenda)

        # remover do veículo
        for encomenda in descarregando:
            self.encomendas.remove(encomenda)

        # retornar encomendas para o ponto
        return descarregando

    def carrega_encomenda(self, encomenda: Encomenda):
        self.visitas_sem_encomenda = 0
        self.encomendas.append(encomenda)

    def liberar(self):
        self.em_transito = True
        self.semaphore.release()

    def loop(self):
        while self.visitas_sem_encomenda < self.S + 1:
            # travar o veículo
            self.em_transito = False
            self.semaphore.acquire()
            # após ser liberado (depois de ser atendido por um ponto):

            # espera o tempo aleatório
            sleep(randint(3, 6))

            # incrementa o ponto
            self.id_ponto_atual = (self.id_ponto_atual + 1) % self.S
            log(
                "veículo {} VIAJANDO para ponto {}".format(self.id, self.id_ponto_atual)
            )

        log("veículo {} FINALIZADO".format(self.id))

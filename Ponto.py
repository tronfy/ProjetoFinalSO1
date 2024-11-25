from __future__ import annotations

from threading import Semaphore, Thread
from random import randint
from time import sleep

from typing import TYPE_CHECKING

from Monitoramento import log

if TYPE_CHECKING:
    from Encomenda import Encomenda
    from Veiculo import Veiculo


class Ponto:
    def __init__(
        self,
        id: int,
        fila_encomendas: list[Encomenda],
        lista_global_veiculos: list[Veiculo],
    ):
        self.id = id
        self.fila_encomendas = fila_encomendas
        self.lista_global_veiculos = lista_global_veiculos
        self.lista_encomendas_recebidas: list[Encomenda] = []
        # self.semaforo = Semaphore(1)

        self.fim = False
        self.veiculo_atual: int = None

        self.thread = Thread(target=self.loop)

    def finalizar(self):
        self.fim = True

    def atender_veiculo(self, veiculo: Veiculo):
        log("ponto {} ATENDENDO veículo {}".format(self.id, veiculo.id))
        self.veiculo_atual = veiculo.id
        # descarrega as encomendas destinadas ao ponto
        encomendas = veiculo.descarrega_encomendas()
        for encomenda in encomendas:
            sleep(randint(1, 3))
            self.lista_encomendas_recebidas.append(encomenda)
            encomenda.entregar()

        # tentar carregar encomendas até encher
        if len(self.fila_encomendas) == 0:
            veiculo.visitas_sem_encomenda += 1
        else:
            while len(veiculo.encomendas) < veiculo.A and self.fila_encomendas:
                encomenda = self.fila_encomendas.pop(0)
                veiculo.carrega_encomenda(encomenda)
                encomenda.carregar(veiculo.id)

        self.veiculo_atual = None

    def loop(self):
        while not self.fim:
            # coletar veículos da lista global em uma fila de atendimento
            fila_veiculos = []
            for veiculo in self.lista_global_veiculos:
                if veiculo.id_ponto_atual == self.id and not veiculo.em_transito:
                    fila_veiculos.append(veiculo)
            for veiculo in fila_veiculos:
                self.lista_global_veiculos.remove(veiculo)

            # atender cada veículo da fila
            for veiculo in fila_veiculos:
                self.atender_veiculo(veiculo)
                # libera e devolve veículo para a lista global
                veiculo.liberar()
                self.lista_global_veiculos.append(veiculo)

        log("ponto {} FINALIZADO".format(self.id))

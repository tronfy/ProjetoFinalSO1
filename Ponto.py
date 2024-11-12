from __future__ import annotations

from threading import Semaphore, Thread
from random import randint
from time import sleep

from typing import TYPE_CHECKING

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
        self.semaforo = Semaphore(1)

        self.thread = Thread(target=self.loop)

    def atender_veiculo(self, veiculo: Veiculo):
        print(
            "ponto {} atendendo veiculo {}".format(self.id, veiculo.id),
            flush=True,
        )
        # descarrega as encomendas destinadas ao ponto
        encomendas = veiculo.descarrega_encomendas()
        for encomenda in encomendas:
            sleep(randint(1, 1))
            self.lista_encomendas_recebidas.append(encomenda)
            encomenda.entregar()

        # tentar carregar encomendas até encher
        while len(veiculo.encomendas) < veiculo.A and self.fila_encomendas:
            encomenda = self.fila_encomendas.pop(0)
            veiculo.carrega_encomenda(encomenda)
            encomenda.carregar(veiculo.id)

    def loop(self):
        while True:
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

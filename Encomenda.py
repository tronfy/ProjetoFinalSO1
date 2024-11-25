from __future__ import annotations


from datetime import datetime
from threading import Thread, Semaphore

from monitoramento import log
from util import format_time


class Encomenda:
    def __init__(self, id: int, id_ponto_origem: int, id_ponto_destino: int):
        self.id = id
        self.id_ponto_origem = id_ponto_origem
        self.id_ponto_destino = id_ponto_destino
        self.horario_origem = datetime.now()
        self.horario_carregamento: datetime = None
        self.horario_destino: datetime = None
        self.id_veiculo: int = None

        self.thread = Thread(target=self.main)
        self.semaforo = Semaphore(0)

    def carregar(self, id_veiculo: int):
        log("encomenda {} CARREGADA por veículo {}".format(self.id, id_veiculo))
        self.id_veiculo = id_veiculo
        self.horario_carregamento = datetime.now()

    def entregar(self):
        self.semaforo.release()

    def main(self):
        self.semaforo.acquire()

        # gerar arquivo de rastro
        self.horario_destino = datetime.now()
        log("encomenda {} ENTREGUE em ponto {}".format(self.id, self.id_ponto_destino))
        with open("encomendas/{}.txt".format(self.id), "w") as f:
            f.write(
                "encomenda {}\norigem: {} ({})\ncoletada por: veículo {} ({})\nentregue em: {} ({})".format(
                    self.id,
                    self.id_ponto_origem,
                    format_time(self.horario_origem.timestamp()),
                    self.id_veiculo,
                    format_time(self.horario_carregamento.timestamp()),
                    self.id_ponto_destino,
                    format_time(self.horario_destino.timestamp()),
                )
            )
        
        # log("encomenda {} FINALIZADA".format(self.id))
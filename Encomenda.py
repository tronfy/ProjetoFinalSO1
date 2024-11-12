from __future__ import annotations


from datetime import datetime
from threading import Thread


class Encomenda:
    def __init__(self, id: int, id_ponto_origem: int, id_ponto_destino: int):
        self.id = id
        self.id_ponto_origem = id_ponto_origem
        self.id_ponto_destino = id_ponto_destino
        self.horario_origem = datetime.now()
        self.horario_carregamento: datetime = None
        self.horario_destino: datetime = None
        self.id_veiculo: int = None

        self.thread = Thread(target=self.loop)

        print(
            "encomenda {} criada em {} de {} para {}".format(
                self.id,
                self.horario_origem,
                self.id_ponto_origem,
                self.id_ponto_destino,
            ),
            flush=True,
        )

    def carregar(self, id_veiculo: int):
        self.id_veiculo = id_veiculo
        self.horario_carregamento = datetime.now()

        print(
            "encomenda {} carregada por {} às {}".format(
                self.id, self.id_veiculo, self.horario_carregamento
            ),
            flush=True,
        )

    def entregar(self):
        self.horario_destino = datetime.now()

        print(
            "encomenda {} entregue por {} às {}".format(
                self.id, self.id_veiculo, self.horario_destino
            ),
            flush=True,
        )

    def loop(self):
        while True:
            pass

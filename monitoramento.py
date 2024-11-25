from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from util import format_time

if TYPE_CHECKING:
    from Encomenda import Encomenda
    from Ponto import Ponto
    from Veiculo import Veiculo

from time import sleep

CLEAR = "\033[H\033[J"

logs: list[str] = []


def log(msg: str):
    str = "[{}] {}".format(format_time(datetime.now().timestamp()), msg)

    logs.append(str)

    with open("out.log", 'a') as f:
        f.write(str + '\n')


def monitorar(
    pontos: list[Ponto], veiculos: list[Veiculo], encomendas: list[Encomenda]
):
    while True:
        sleep(0.1)

        # exibir status
        buf = "PONTOS:\n"
        for ponto in pontos:
            fila_veiculos = [
                v.id
                for v in veiculos
                if v.id_ponto_atual == ponto.id and v.thread.is_alive()
            ]
            buf += "ponto {};  recebidas:[ {} ];  a_enviar:[ {} ];  sendo_atendido: {};  fila:[ {} ];\n".format(
                ponto.id,
                " ".join([str(e.id) for e in ponto.lista_encomendas_recebidas]).ljust(22),
                " ".join([str(e.id) for e in ponto.fila_encomendas]).ljust(16),
                str(ponto.veiculo_atual).ljust(4),
                " ".join(str(id) for id in fila_veiculos).ljust(8)
            )

        # exibir ultimos logs
        buf += "\nLOGS:\n"
        buf += "\n".join(logs[-15:])

        print(CLEAR + buf, flush=True)

        # verificar se deve encerrar
        if all([not p.thread.is_alive() for p in pontos]):
            break

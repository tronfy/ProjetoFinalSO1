# Projeto Final Rede de Entregas utilizando Threads

Este projeto se trata de uma aplicação concorrente que simula o comportamento de uma rede de entregas, em que encomendas são transportadas por veículos de ponto de redistribuição a outro.

## Funcionalidades

- Passagem de parâmetros por linha de comando.
- Utiliza Threads para Veículos, Pontos e Encomendas.
- Encomendas e Veículos inciam em pontos aleatórios
- Encomendas entram em fila ao chegarem nos Pontos de Redistribuição.
- Veículos entram em fila ao chegarem nos Pontos de Redistribuição.
- Tempos de viagem e de descargar dos veículos aleatório.
- Rastreio de cada encomenda, com seus respectivos logs.
- Monitoramento em tempo real do sistema.
- Saída global out.log, com todo o histórico da aplicação. 

## Conteúdo

- [Detalhes](#detalhes)
- [Instalação](#instalação)
- [Uso](#uso)
- [Créditos](#créditos)

## Detalhes

Há três Classes Principais, Encomendas, Veículos, e Pontos de Redistribuição. Em todas são utilizadas Threads.

Os Pontos são responsáveis por atender os Veículos, decarregando as encomendas (caso seu destino for o ponto atual) e carregando outras novas. 

O Veículo trava ao chegar em um ponto, este é responsável por descarregar e carregar o veículo com novas encomendas, e logo após é destravado e viaja ao próximo ponto. A ordem da fila é mantida pela variável `veiculo.em_transito`, que é alterada para `False` no fim da viagem (3 a 6s).

Encomendas são criadas travadas, e destravadas quando são entregues. Ao destravar, criam um arquivo de log individual.

Ao final, quando todas as encomendas são entregues e suas threads finalizadas, os veículos dão uma última volta pelos pontos e como não carregam nenhuma encomenda, são finalizados também. 

Uma vez todos os veículos finalizados, a thread principal chama `ponto.finalizar()`, o que finaliza as threads de todos os pontos.

## Instalação

Clone esse repositório:

```bash

git clone https://github.com/tronfy/ProjetoFinalSO1.git

cd ProjetoFinalSO1

```

## Uso

Passe os parâmetros na ordem S C P A, onde:
S (nº Pontos de Redistribuição)
C (nº Veículos)
P (nº Encomendas)
A (nº de Encomendas suportadas em cada Veículo)

```bash

python main.py <S> <C> <P> <A>

```

Tenha certeza que P >> A >> C.

```bash

python main.py 5 3 20 5

```

## Créditos

Curso de Sistemas Operacionais I ministrado por Prof. Dr. Caetano Mazzoni Ranieri no DEMAC, IGCE, Unesp, Rio Claro.
Desenvolvido por Nícolas Schmidt e Edgar Galvão.
Bacharelado em Ciências da Computação, 2024.

# Projeto Final Rede de Entregas utilizando Threads

Este projeto se trata de uma aplicação concorrente que simula o comportamento de uma rede de entregas, em que encomendas são transportadas por veículos de ponto de redistribuição a outro.

## Funcionalidades

- Passagem de parâmetros por linha de comando.
- Utiliza Threads para Veículos, Pontos e Encomendas.
- Encomendas e Veículos inciam em pontos aleatórios
- Encomendas entram em fila ao chegarem nos Pontos de Redistribuição.
- Veículos entram em fila ao chegarem nos Pontos de Redistribuição.
- Tempos de viagem e de descargar dos veículos aleatório.
- Rastreio de cada encomenda.

## Conteúdo

-[Detalhes] (#Detalhes) -[Instalação] (#Instalação) -[Uso] (#Uso) -[Créditos] (#Créditos)

## Detalhes

Há três Classes Principais, Encomendas, Veículos, e Pontos de Redistribuição. Em todas são utilizadas Threads.
Os pontos são responsáveis por atender os Veículos, decarregando as encomendas (caso seu destino for o ponto atual) e carregando outras novas. Nesse processo é o utilizado um semáforo QUE TRAVA EM TAL MOMENTO e DESTRAVA E TAL MOMENTO.

O Veículo trava ao chegar em um ponto, este é responsável por descarregar e carregar o veículo com novas encomendas.

Encomendas são criadas travadas, e destravadas quando são entregues.

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

python main.py [S] [C] [P] [A]

```

Tenha certeza que P >> A >> C.

```bash

python main.py 5 3 6 5

```

## Créitos

Curso de Sistemas Operacionais I ministrado por Prof. Dr. Caetano Mazzoni Ranieri no DEMAC, IGCE, Unesp, Rio Claro.
Desenvolvido por Nícolas Schmidt e Edgar Galvão.
Bacharelado em Ciências da Computação, 2024.

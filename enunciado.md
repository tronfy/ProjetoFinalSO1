possíveis soluções pra incrementar ponto do veiculo:
solução 1:

- Veículo tem acesso à lista global de Pontos

solução 2:

- Ponto tem acesso à lista global de Veículos
- Veículo só tem id_ponto_atual
- Ponto só atende veículos que estão que v.id_ponto_atual == p.id
- como lidar com a fila? lista de ids? meio gambiarra

solução 3:

- Ponto tem acesso à lista global de Veículos
- Veículo só tem id_ponto_atual
- Ponto remove (coloca na fila local do ponto) veiculos da lista global quando v.id_ponto_atual == p.id
- ponto atende veiculos na ordem da fila
- ponto chama destravar_veiculo(), o que incrementa v.id_ponto_atual
- ponto devolve veiculo pra lista global

Main:

- variáveis:
  - S (pontos de redistribuição)
  - C (veículos que representam os meios de transporte)
  - P (encomendas a serem entregues)
  - A (espaços de carga em cada veículo, todas as encomendas ocupam exatamente 1 espaço de carga)
  - Arquivo relatorio
  - fila de pontos de redistribuição

Encomenda:

- atributos:
  - id (sequencial)
  - ponto de origem (aleatório)
  - ponto de destino (aleatório)
  - horário em que chegou ao ponto de origem
  - horário que foi carregada no veículo
  - identificador do veículo
  - horário em que foi descarregada no ponto de destino
- métodos:
  - gravar arquivo de rastro (id encomenda, origem e destino, horario de chegada ponto origem, horario chegada ponto destino, horario de desgarga)

Veiculo:

- atributos:
  - id (sequencial)
  - ponto atual (inicializado aleatoriamente)
  - encomendas (lista com capacidade A)
- métodos:
  - carregar encomenda (tempo aleatório)
  - descarregar encomenda (tempo aleatório)
- loop:
  - percorrer pontos de redistribuição sequencialmente (fila circular), aguardando
    atendimento em cada ponto para carregar e descarregar encomendas

Ponto de redistribuição:

- atributos:
  - id (sequencial)
  - fila de encomendas aguardando despacho
  - fila de veículos aguardando atendimento (um veículo atendido por vez)
  - lista de encomendas recebidas (este é seu ponto de destino)
  - Semaforo
- métodos:
  - entregar encomenda (remover da fila de encomendas aguardando despacho)
  - receber encomenda (adicionar na lista de encomendas recebidas)
  - receber veículo (adicionar na fila de veículos aguardando atendimento)
  - atender veículo (entregar/receber encomendas e remover da fila de veículos aguardando atendimento)
- loop:
  - atender veículos em ordem de chegada

PROJETO DA DISCIPLINA

- Desenvolver uma aplicação concorrente que simule o comportamento de uma rede de
  entregas, em que encomendas são transportadas por veículos de um ponto de
  redistribuição até outro.
- A sincronização deve ser feita com uso de semáforos e variáveis de trava.
- Os trabalhos serão realizados em duplas ou, excepcionalmente, em grupos de 3 alunos.

ENUNCIADO

- Para fins de simplificação, considere que os pontos de redistribuição estão organizados
  sequencialmente.
- Na sua implementação, suponha que:
  - Há S pontos de redistribuição.
  - Há C veículos que representam os meios de transporte.
  - Há P encomendas a serem entregues.
  - Há A espaços de carga em cada veículo (todas as encomendas ocupam exatamente
    1 espaço de carga).
  - Deve-se assegurar que P >> A >> C.
- O programa deve admitir argumentos de entrada determinando S, C, P e A ao iniciar a
  aplicação. O thread principal deverá receber esses argumentos e gerar um thread para cada
  uma das P encomendas, cada um dos C veículos e cada um dos S pontos de redistribuição
  especificados (numerá-los sequencialmente para identificação).
- Os veículos podem partir de pontos distintos e aleatórios, definidos na inicialização dos seus threads. A rede de distribuição admite que apenas um veículo seja atendido em um ponto por vez. Se um ponto estiver vazio (sem encomendas aguardando despacho), o veículo segue para o próximo ponto de redistribuição.

- As encomendas, ao chegarem a um ponto de redistribuição, ficam organizadas em uma fila
  controlada pelo ponto de redistribuição. Ao chegar no destino, cada encomenda é
  descarregada (tempo aleatório) e seu thread finaliza.
- O tempo de viagem entre um ponto de redistribuição e outro é aleatório e não fixo para
  todos os veículos. Um veículo pode ultrapassar outro veículo durante a viagem e chegar
  antes ao próximo ponto de redistribuição.
- Enquanto houver encomendas para serem entregues, os veículos continuam circulando
  entre os pontos. Quando um veículo chega ao último ponto, ele é direcionado novamente
  ao primeiro ponto (uma fila circular).
- Argumentos de entrada fornecidos aos threads das encomendas indicam os seus pontos de
  origem e destino. Esses argumentos são determinados aleatoriamente quando da criação
  dos threads de cada encomenda.
- Quando todas as encomendas tiverem sido entregues, os veículos param de circular e a
  aplicação acaba.
- As saídas do programa deverão ser:

1. Uma tela para monitoramento em tempo real das encomendas, pontos de
   redistribuição e veículos.
2. Os arquivos de rastro das encomendas gravados em disco.
   a. Cada encomenda gera um arquivo de rastro contendo o número da
   encomenda, seus pontos de origem e destino, o horário que chegou ao
   ponto de origem, o horário que foi carregada no veículo, o identificador
   desse veículo e o horário em que foi descarregada no ponto de destino.

ENTREGA

- Código-fonte, preferencialmente no Github ou repositório semelhante (será considerado o
  último commit antes do prazo de entrega).
- Incluir readme detalhando a implementação realizada.
- Apresentação em sala de aula de cada trabalho.
- Prazo: 25/11 (data da apresentação).

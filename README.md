# Orientações gerais

O trabalho de implementação da disciplina de SO (UnB), a ser desenvolvido em grupo com quatro
componentes (Boris Marinho, Guilherme Andreúce, Pedro Henrique e Roberta Costa) compreenderá as seguintes fases:
- Estudo teórico relacionado ao assunto do trabalho;
- Apresentação da solução teórica dada ao problema;
- Implementação da solução proposta;
- Apresentação e explicação detalhada do código-fonte implementado;
- Relatório explicando o processo de construção e o uso da aplicação.

# Orientações específicas
## Problema
Implementação de um pseudo-SO multiprogramado, composto por um Gerenciador de Processos,
por um Gerenciador de Memória e por um Gerenciador de Entrada/Saída. O gerenciador de processos
deve ser capaz de aplicar o algoritmo de escalonamento definido por meio de parâmetro pelo usuário do SO.
O gerenciador de memória deve garantir que um processo não acesse as regiões de memória de um outro
processo, e que o algoritmo de substituição de página seja adequadamente usado. E o gerenciador de
entrada/saída deve ser responsável por administrar o algoritmo especificado para a busca em disco. Cada
módulo será testado de acordo com as especificações determinadas abaixo. Além disso, o pseudo-SO deve
receber como parâmetro um inteiro e um arquivo texto, por exemplo $ 1 processes.txt. O inteiro determina
qual módulo deve ser ativado (no exemplo dado significa que será ativado o módulo de processos, pois foi o
inteiro 1), e o arquivo texto (com extensão .txt) repassa os dados de entrada necessários para a execução do
módulo escolhido. Os detalhes para a implementação desse pseudo-SO são descritos nas próximas seções.

### Módulo de Gerência de Processos
Neste módulo a equipe deve implementar um conjunto de algoritmos de escalonamento de CPU e escrever
um programa que calcula uma série de estatísticas baseada nestes algoritmos. Os algoritmos de
escalonamento a serem implementados são os seguintes:
- FIFO: First-In, First-Out
- SJF: Shortest Job First
- RR: Round Robin (com quantum = 2)
O módulo de gerência de processos deverá ler da entrada padrão uma lista de processos com seus
respectivos tempos de chegada e de duração, e deverá imprimir na saída padrão uma tabela contendo os
valores para as seguintes métricas:
- Tempo médio de execução total do processo - turnaround;
- Tempo médio de resposta;
- Tempo médio de espera.
Tempo de execução total do processo é a quantidade de tempo necessária para executar totalmente um
processo, ou seja, é o tempo total entre a criação de um processo e seu término. Tempo de resposta é a
quantidade de tempo entre a requisição de execução de um programa (quando ele é colocado na fila de
pronto) e o seu tempo de ir para a execução (sistema de compartilhamento de tempo), isso significa que é o
tempo que o processo demora para produzir cada resposta a uma requisição (assim, vamos considerar que é
o tempo decorrido entre uma ida e outra para a CPU. Essa métrica é importante para processos interativos).
E tempo de espera é a quantidade total de tempo que um processo aguardou na fila de prontos esperando
para ser escalonado, ou seja, é o tempo que processo ficou esperando na fila de prontos. 

#### Descrição da Entrada do Módulo de Gerência de Processos
O arquivo texto é composto por uma série de pares de números inteiros separados por um espaço em branco
indicando o tempo de chegada e a duração de cada processo. A entrada termina com o fim do arquivo. A
ativação deste módulo deve ser com os parâmetros $ <executável> 1 <nomeArquivoTexto.txt>

#### Descrição da Saída do Módulo de Gerência de Processos
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e os valores das três métricas
solicitadas. Cada linha apresenta a sigla do algoritmo e os valores médios (com uma casa decimal) para tempo total de
execução, tempo de resposta e tempo de espera, exatamente nesta ordem, separados por um espaço em
branco.

#### Módulo de Gerência de Memória
Neste módulo a equipe deve escrever um programa para simular o funcionamento dos principais algoritmos
de substituição de páginas estudados na disciplina. Os algoritmos de substituição de páginas a serem
implementados são os seguintes:
- FIFO (First In, First Out);
- Segunda Chance (com o bit R sendo zerado a cada 3 referências feitas à memória);
- LRU: (Least Recently Used ou Menos Recentemente Utilizado).
O programa deverá ler da entrada padrão um conjunto de número inteiros, dos quais o primeiro número
representa a quantidade de quadros de memória disponíveis na RAM e os demais representam a sequência
de referências às páginas, sempre um número por linha.
Além disso, o programa deverá imprimir na saída o número de faltas de páginas obtido com a utilização de
cada um dos algoritmos.

#### Descrição da Entrada para o Módulo de Gerência de Memória
A entrada é composta por uma série de números inteiros, um por linha, indicando, primeiro a quantidade de
quadros (frames) disponíveis na memória RAM e, em seguida, a sequência de referências à memória. A
ativação deste módulo deve ser com os parâmetros $ <executável> 2 <nomeArquivoTexto.txt>

#### Descrição da Saída para o Módulo de Gerência de Memória
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de
página obtidas com a utilização de cada um deles.

#### Módulo de Gerência de Entrada/Saída
Neste módulo a equipe deve escrever um programa para simular o funcionamento dos principais algoritmos
de escalonamento de disco estudados na disciplina. Os algoritmos de escalonamento de disco a serem
implementados são os seguintes:
- FCFS (First Come, First Serve);
- SSF (ou SSTF – braço inicialmente para baixo);
- SCAN.
O programa deverá ler da entrada padrão um conjunto de número inteiros, no qual o primeiro número
representa a quantidade de cilindros no disco, o segundo número representa o cilindro sobre o qual a cabeça
de leitura do disco está inicialmente posicionada, e os demais representam uma sequência de requisições de
acesso a serem atendidas, sempre um número por linha.
O programa deverá imprimir na saída o número total de cilindros percorridos pela cabeça de leitura para
atender todas as requisições solicitadas utilizando cada um dos algoritmos.

#### Descrição da Entrada do Módulo de Entrada/Saída
A entrada é composta por uma série de números inteiros, um por linha, indicando, primeiro o número do
último cilindro no disco (os cilindros variam de 0 até este número), o cilindro sobre o qual a cabeça de leitura
está inicialmente posicionada e a sequência de requisições de acesso. A ativação deste módulo deve ser
com os parâmetros $ <executável> 3 <nomeArquivoTexto.txt>

#### Descrição da Saída do Módulo de Entrada/Saída
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade total de
cilindros percorridos pela cabeça de leitura para atender todas as requisições de acesso ao disco.

### Estrutura do Programa
Espera-se que o programa seja estruturado em, pelo menos, quatro grandes módulos: kernel,
processo, memória e entrada/saída. Esses modelos devem ser:
-Módulo Kernel – contém as chamadas para os demais módulos.
- Módulo de Processos – classes e estruturas de dados relativas ao processo. Basicamente,
mantém informações específicas do processo.
- Módulo de Memória – provê uma interface de abstração de memória RAM.
- Módulo de Entrada/Saída – trata a alocação do braço do disco para realização de escrita/leitura
nos blocos do disco para os processos.
É importante ressaltar também que outros módulos podem ser utilizados, caso sejam necessários.

### Estudo Teórico para a Solução
Cada equipe deverá buscar a solução para o compartilhamento de recursos e a sincronização de
processos (ou threads), quando se fizer necessário, de acordo com o problema proposto. É responsabilidade
de cada grupo estudar a maneira mais eficiente para implementar o pseudo-SO. Contudo, é importante
ressaltar que para o problema de compartilhamento de recursos não há soluções mágicas, as soluções
possíveis são exatamente as mesmas vistas em sala de aula: semáforos (baixo nível), monitores (alto nível,
mas devem ser implementados pela linguagem de programação, pois o compilador deve reconhecer o tipo
monitor) e troca de mensagens (usadas preferencialmente para garantir a sincronização entre processos em
máquinas diferentes, também podem ser usadas para processos na mesma máquina. Nesse caso, as
mensagens trocadas passam por toda a pilha de protocolos como se estivessem sendo enviadas para outra
máquina).

# Instruções de compilação


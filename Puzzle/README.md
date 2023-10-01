# Apresentação do Trablho Quebra cabeça 3x3
Esse trabalho tem como objetivo mostrar o desempenho do algoritmo A* utilizando a linguágem Python para demostração do problema.

## Explicando o Algoritmo A*
O algoritmo A* ele simplesmete é uns dos algoritmo de busca que utilizamos em IA para poder encontrar uma Estado Objetivo onde esse estádo Objetivo nem sempre é a resposta e sim as ações tomadas até chegar a resposta.

* Como funciona o Algoritmo A* ?
    ele funciona da seguinte forma precisamos determinas dois valores para encontar o valor da heuristica e o valor dos nós. Para determinar o valor da Heuristica nesse problema  a gente pode fazer a comparação de matrix, fazendo a comparação de matriz conseguimos determinar o valor de h(x) e o valor do nó(g(x)) vamos iniciar com 0

    A heuristica é determinada pela acuracia se tiver uma acuracia boa a heuristica é excelente caso contrario não temos uma heuristica boa com isso o A* vai ser lento e muito ruim.

    Sabendo disso vamos percorrer a arvore e gerar novos ramos para identificar o melhor caminho, para saber qual é o menor caminho a heuristica do problema tem que tender a 0 assim vamos identificar que realmente chegamos ao resultado do nosso problema. 

    para gerar os nosso nós primeiro precisamos de uma heap(ponto de memoria) onde vamos alocar os dados para consultamos caso o ramo que estamos descendo não for compativel. A regra é feita da seguinte maneira, vamos ter que busca os melhores nós para identificar o menor nó e a soma de f = h + g ela vai nos dizer se aquele ramo que estamos abrindo é bom ou ruim comparando com os anteriores.

    Assim que for selecionado o melhor nó vamos entrar nele e descer mais até achar a solução, vamos fazer as combinações, as combinações são feita da seguinte forma, vamos dar para o programa as regras que podemos movimentar, como no Puzzle 3x3 temos as seguintes combinações subir,descer,esquerda,direita como estamos trabalhando como uma matriz, então precisamos identificar o que é subir,descer,esquerda e direita para assim podermos movimentar.

    Para fazer a movimentação da matriz, atribuimos valores a subir que é [-1,0] descer [1,0] esquerda [0,-1] direita é [0,1], pronto temos a movimentaçao da nossa matriz, precisamos dar a regra que não podemos pular nenhum número que não esteja nessa direção para o campo vazio.

    Final tempo gasto para executar 5418 em 869864 ms = 14 Minutos

### Como utilizar os programas ?
* Para utilização vamos precisar chamar um dos dois tipos de argumentos
    1. result_puzzle possui dois parametros um para colocar o quebra cabeça e outro para colocar qual vai ser o A* com uma determinada heuristica exemplo a normal que comprar só a quantidade de casas faltantes
    ```python
        result_puzzle([[0,5,3],[6,1,7],[2,8,4]],main_not_manhattan)
    ```
    2. result_with_test_load ele faz uma sequencia de test onde vc determina a quantidade de processos que vão ser utilizado exemplo este
    ```python

        listNova = [[[0,5,3],[6,1,7],[2,8,4]],
               [[2,3,7],[4,6,8],[5,0,1]],
               [[8,2,6],[3,4,0],[5,7,1]]]

        result_with_test_load(listNova,main_not_manhattan)

    ```
    3. result_with_list_random esse gerador cria lista aleatorias para fazer o teste, você pode colocar quantos números quiser, por exemplo esté, e ele tbm tem dois argumentos um para quantidade de arrays a gerar e outra para a heuristica que irá ser utilizada, quando não se passa nada ele automaticamente usa a de manhattan
    ```python
        result_with_list_random(5)
    ``````
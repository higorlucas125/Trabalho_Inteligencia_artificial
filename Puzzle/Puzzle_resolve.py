from copy import deepcopy
from colorama import Fore, Back,Style
from itertools import permutations
import time
from pprint import pprint as pp
from Generation_puzzle import main as generation_matriz

TEST = [[6,2,8],[4,7,1],[0,3,5]]

# [[7,6,8],[3,4,5],[1,2,0]]
NOVO=[[1,2,3],[4,5,6,],[0,7,8]]

DIRECTIONS = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
# [[1,2,3],[4,5,6],[7,8,0]]

END = [[0,1,2],[3,4,5],[6,7,8]]


typeStyleTable = Style.BRIGHT
colorTable = Fore.MAGENTA

# unicode for draw puzzle in command promt or terminal
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250c'

middle_junction = '\u253c'
top_junction = '\u252c'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251c'

#bar color
bar = typeStyleTable + colorTable + '\u2502' + Fore.RESET + Style.RESET_ALL
dash = '\u2500'

#Line draw code
first_line = typeStyleTable + colorTable + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL

middle_line = typeStyleTable + colorTable + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL

last_line = typeStyleTable + colorTable + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL

def print_puzzle(array):
    print(first_line)
    for a in range(len(array)):
        for i in array[a]:
            if i == 0:
                print(bar, Back.RED + ' ' + Back.RESET, end=' ')
            else:
                print(bar, i, end=' ')
        print(bar)
        if a == 2:
            print(last_line)
        else:
            print(middle_line)

def get_pos(puzzle_end,element):
    for row in range(len(puzzle_end)):
        if element in puzzle_end[row]:
           return(row,puzzle_end[row].index(element))

def heuristic(puzzle):
    if len(puzzle) != len(END) or len(puzzle[0]) != len(END[0]):
        raise ValueError("As matrizes devem ter o mesmo tamanho")

    count = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != END[i][j]:
                count += 1

    return count


def euclidianCost(puzzle):
    cost = 0
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            pos = get_pos(END,puzzle[row][col])
            sum_value = abs(row - pos[0]) + abs(col - pos[1])
            cost += sum_value
    return cost

def get_best_node(open_set):
    firstInter = True

    for node in open_set.values():
        if firstInter or node.f() < bestF:
            firstInter = False
            bestNode = node
            bestF = bestNode.f()
    return bestNode

def get_adj_node_not_manhattan(node):
    listNode = []
    emptyPos = get_pos(node.current_node, 0)

    for dir in DIRECTIONS.keys():
        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
        if 0 <= newPos[0] < len(node.current_node) and 0 <= newPos[1] < len(node.current_node[0]):
            newState = deepcopy(node.current_node)

            postion_zero_x = emptyPos[0]
            postion_zero_y = emptyPos[1]

            position_item_change_x = newPos[0]
            position_item_change_y = newPos[1]

            newState[postion_zero_x][postion_zero_y] = node.current_node[position_item_change_x][position_item_change_y]
            newState[position_item_change_x][position_item_change_y] = 0
            
            listNode.append(Node(newState, node.current_node, node.g + 1, heuristic(newState), dir))

    return listNode
    

def get_adj_node(node):
    listNode = []
    emptyPos = get_pos(node.current_node, 0)

    for dir in DIRECTIONS.keys():
        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
        if 0 <= newPos[0] < len(node.current_node) and 0 <= newPos[1] < len(node.current_node[0]):
            newState = deepcopy(node.current_node)

            postion_zero_x = emptyPos[0]
            postion_zero_y = emptyPos[1]

            position_item_change_x = newPos[0]
            position_item_change_y = newPos[1]

            newState[postion_zero_x][postion_zero_y] = node.current_node[position_item_change_x][position_item_change_y]
            newState[position_item_change_x][position_item_change_y] = 0
            
            listNode.append(Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir))

    return listNode




class Node:
    def __init__(self,current_node,previous_node,g,h,dir):
        self.current_node = current_node
        self.previous_node = previous_node
        self.g = g
        self.h = h
        self.dir = dir
    def f (self):
        return self.g + self.h
    
    def __str__(self):
        return f'current_node = {self.current_node} \n previous_node = {self.previous_node} \n g = {self.g} \n h= {self.h}\n direcion = {self.dir} '

def move(arg):
    switcher = {
        'U':'CIMA',
        'R':'DIREITA',
        'L':'ESQUERDA',
        'D':'BAIXO'
    }

    return switcher.get(arg) if switcher.get(arg) is not None else ''

def buildPath(closedSet):
    node = closedSet[str(END)]
    branch = list()

    while node.dir:
        branch.append({
            'dir': node.dir,
            'node': node.current_node
        })
        node = closedSet[str(node.previous_node)]
    branch.append({
        'dir':'',
        'node': node.previous_node
    })
    branch.reverse()

    return branch


def main_not_manhattan(puzzle):
    open_set = {str(puzzle): Node(puzzle,puzzle,0,heuristic(puzzle),"")}
    closed_set = {}
    contador = 0

    while len(open_set) != 0:
        test_best_node = get_best_node(open_set)
        closed_set[str(test_best_node.current_node)] = test_best_node
        
        if test_best_node.current_node == END:
            print("Quantidade de execuções nescessaria para trazer o resultado: ",contador)
            return buildPath(closed_set)
        
        # Andar com o nó
        adj_node = get_adj_node(test_best_node)
        for node in adj_node:

            if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[str(node.current_node)].f() < node.f():
                continue
            open_set[str(node.current_node)] = node
            contador +=1
        #print(len(open_set))
        del open_set[str(test_best_node.current_node)]
    
    print("Finalizado sem solução")

def main(puzzle):
    open_set = {str(puzzle): Node(puzzle,puzzle,0,euclidianCost(puzzle),"")}
    closed_set = {}
    contador = 0

    while len(open_set) != 0:
        test_best_node = get_best_node(open_set)
        closed_set[str(test_best_node.current_node)] = test_best_node
        
        if test_best_node.current_node == END:
            print("Quantidade de execuções nescessaria para trazer o resultado: ",contador)
            return buildPath(closed_set)
        
        # Andar com o nó
        adj_node = get_adj_node(test_best_node)
        for node in adj_node:

            if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[str(node.current_node)].f() < node.f():
                continue
            open_set[str(node.current_node)] = node
            contador +=1
        print(len(open_set))
        del open_set[str(test_best_node.current_node)]
    
    print("Finalizado sem solução")


def result_puzzle (puzzle,executKindHeuristic=main):
    puzzle_result = executKindHeuristic(puzzle)

    print()
    print(dash + dash + right_junction, "Entrada", left_junction + dash + dash)

    for result in puzzle_result:
        if result ['dir'] != '':
            letter = move(result['dir'])
            print(dash + dash + right_junction, letter, left_junction + dash + dash)
        print_puzzle(result['node'])
        print()
    
    print(dash+dash + right_junction, 'Acima está a saida', left_junction + dash + dash)

    print('Quantidade de movimentos que será nescessario até o final',(len(puzzle_result) - 1))

    return puzzle_result

def result_with_list_random (quantidade_de_vetor,executKindHeuristic=main):
    tempo_inicial_geral = time.time()
    
    for puzzle in generation_matriz(quantidade_de_vetor,6):
        
        tempo_inicial = time.time()
        
        result_puzzle(puzzle,executKindHeuristic)

        tempo_final = time.time()

        tempo_de_execucao = round((tempo_final - tempo_inicial)*1000)

        print(f'Inicio {puzzle} e tempo de execucao {tempo_de_execucao} ms')
    
    tempo_final_geral = time.time()

    tempo_de_execucao_geral = round((tempo_final_geral - tempo_inicial_geral)*1000)

    print(f'Tempo gasto no algoritmo para {quantidade_de_vetor} tempo foi {tempo_de_execucao_geral} ms')


def result_with_test_load(insertBaseTest,executKindHeuristic=main):
    tempo_inicial_geral = time.time()
    
    for puzzle in insertBaseTest:
        
        tempo_inicial = time.time()
        
        result_puzzle(puzzle,executKindHeuristic)

        tempo_final = time.time()

        tempo_de_execucao = round((tempo_final - tempo_inicial)*1000)

        print(f'Inicio {puzzle} e tempo de execucao {tempo_de_execucao} ms')
    
    tempo_final_geral = time.time()

    tempo_de_execucao_geral = round((tempo_final_geral - tempo_inicial_geral)*1000)

    print(f'Tempo gasto no algoritmo para {len(insertBaseTest)} tempo foi {tempo_de_execucao_geral} ms')

if __name__ =='__main__':

    # result_with_matriz_not_manhattan(TEST)

    # result_puzzle([[0,5,3],[6,1,7],[2,8,4]],main_not_manhattan)

    # result_with_matriz([[1,2,3],[4,6,0],[7,8,5]])
    # result_with_qtd(20)

    # listNova = [[[0,5,3],[6,1,7],[2,8,4]],
    #            [[2,3,7],[4,6,8],[5,0,1]],
    #            [[8,2,6],[3,4,0],[5,7,1]]]

    # result_with_test_load(listNova,main_not_manhattan)

    result_with_list_random(5)


# Quantidade de movimentos que será nescessario até o final 25
# Inicio [[8, 2, 6], [3, 4, 0], [5, 7, 1]] e tempo de execucao 193 ms
# Tempo gasto no algoritmo para 3 tempo foi 990 ms

# Quantidade de movimentos que será nescessario até o final 25
# Inicio [[2, 3, 7], [4, 6, 8], [5, 0, 1]] e tempo de execucao 214 ms
# Quantidade de execuções nescessaria para trazer o resultado:  4200

# Quantidade de movimentos que será nescessario até o final 26
# Inicio [[0, 5, 3], [6, 1, 7], [2, 8, 4]] e tempo de execucao 584 ms
# Quantidade de execuções nescessaria para trazer o resultado:  4482
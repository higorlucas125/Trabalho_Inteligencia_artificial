from itertools import permutations

def solvable(tiles):
    count = 0
    for i in range(8):
        for j in range(i+1, 9):
            if tiles[j] and tiles[i] and tiles[i] > tiles[j]:
                count += 1

    is_solvable = count % 2 == 0

    if is_solvable:
        difficulties = {'0': 'trivial',
                        '2': 'easy',
                        '4': 'medium',
                        '6': 'hard'
                        }
        difficulty = difficulties.get(str(count), 'very hard')
        return [difficulty, count, is_solvable]

    return [count, is_solvable]

def generate_tiles(count=2):
    """Generate solvable tiles for the 3x3 puzzle."""
    tile_candidates = list(permutations(list(range(9))))
    good_tiles = []
    for tile_candidate in tile_candidates:
        if solvable(tile_candidate)[-1]:
            good_tiles.append(tile_candidate)
    return good_tiles


def choose_difficulty(tiles, level=2):
    """Choose difficulty for the 3x3 puzzle, default level is easy (2)."""
    labelled_tiles = []
    for tile in tiles:
        labelled_tiles.append({"tile": tile,
                               "label": solvable(tile)
                               })
    level_tiles = []
    for tile_dict in labelled_tiles:
        if tile_dict['label'][1] == level:
            level_tiles.append(tile_dict)
    return level_tiles


def return_matriz(seq):
    # Inicialize uma matriz vazia 3x3
    matriz = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    # Preencha a matriz com os elementos da sequência
    for i in range(3):
        for j in range(3):
            matriz[i][j] = seq[i * 3 + j]

    return matriz

def main(qtd=10,level=2):
    tiles = generate_tiles()
    dados = choose_difficulty(tiles,level)
    qtd_executado = qtd
    list_print = []
    cont = 0
    
    for d in dados:
        puzzle = return_matriz(d['tile'])
        list_print.append(puzzle)
        if cont == qtd_executado:
            break
        cont +=1
    return list_print

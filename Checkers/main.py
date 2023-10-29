import pygame
from pygame.locals import *
from checkers.globalCounter import GlobalCounter

# from checkers import WIDTH , HEIGHT
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED,WHITE,SCREEN_WIDTH,SCREEN_HEIGHT

from checkers.game import Game

from minimax.algorithm import minimax

from minimax.algorithm import alphabeta

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_caption('Checkers')

def finish_game(color):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Jogador campeão " + color, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

def get_row_col_from_mouse(pos):
    x,y  = pos 
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def playerVsPlayer():


    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    # piece= board.get_piece(0,1)
    # board.move(piece,4,3)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            finish_game(game.winner())
            run = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)
                # if game.turn == RED:
                #     game.select(row,col)
        
        game.update()
    
    pygame.quit()


def playVsMiniMax ():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    # piece= board.get_piece(0,1)
    # board.move(piece,4,3)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            contador = GlobalCounter()
            value,new_board = minimax(game.get_board(),1,WHITE,game,contador,float("-inf"),float("inf"))
            contador.set_chousen_board(new_board)
            print('{}{}{}',contador,minimax.__name__,value)
            game.ai_move(new_board)

        if game.winner() != None:
            finish_game(game.winner())
            run = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)
                # if game.turn == RED:
                #     game.select(row,col)
        
        game.update()
    
    pygame.quit()

def playVsAlphBeta ():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    # piece= board.get_piece(0,1)
    # board.move(piece,4,3)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            contador = GlobalCounter()
            value,new_board = alphabeta(game.get_board(),4,WHITE,game,contador,float("-inf"),float("inf"))
            contador.set_chousen_board(new_board)
            print('{}{}{}',contador,minimax.__name__,value)
            game.ai_move(new_board)

        if game.winner() != None:
            finish_game(game.winner())
            run = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)
                # if game.turn == RED:
                #     game.select(row,col)
        
        game.update()
    
    pygame.quit()

def CpuVsCpu(algorithm):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == RED:
            contador = GlobalCounter()
            value,new_board = algorithm(game.get_board(),4,False,game,contador,float("-inf"),float("inf"))
            contador.set_chousen_board(new_board)
            print(contador,minimax.__name__,value)
            game.ai_move(new_board)
            pygame.time.delay(1000)
        
        # if game.turn == WHITE:
            # contador = GlobalCounter()
            # value,new_board = algorithm(game.get_board(),4,True,game,contador,float("-inf"),float("inf"))
            # contador.set_chousen_board(new_board)
            # print(contador,minimax.__name__,value)
            # game.ai_move(new_board)
        #     pygame.time.delay(1000)
        
        if game.winner() != None:
            finish_game(game.winner())
            run = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.turn == WHITE:
                    pos = pygame.mouse.get_pos()
                    if pos != None:
                        contador = GlobalCounter()
                        value,new_board = algorithm(game.get_board(),4,True,game,contador,float("-inf"),float("inf"))
                        contador.set_chousen_board(new_board)
                        print(contador,minimax.__name__,value)
                        game.ai_move(new_board)
                # if game.turn == RED:
                #     game.select(row,col)
        
        game.update()
    
    pygame.quit()

        

def main(jogada):
    match jogada:
        case 'PP':
            playerVsPlayer()
            return
        case 'PM':
            playVsMiniMax()
            return
        case 'PA':
            playVsAlphBeta()
            return
        case 'CM':
            CpuVsCpu(minimax)
            return
        case 'CA':
            CpuVsCpu(alphabeta)
            return
        case default: 
            return "Não foi possivel selecionar"
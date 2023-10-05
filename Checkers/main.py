import pygame
from pygame.locals import *

# from checkers import WIDTH , HEIGHT
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED

from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')


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
    text = font.render("Joga dor campeão " + color, 1, (10, 10, 10))
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

def main():
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
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)
                # if game.turn == RED:
                #     game.select(row,col)
        
        game.update()
    
    pygame.quit()


main()
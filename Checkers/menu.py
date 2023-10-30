import pygame,sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280,720))
pygame.display.set_caption=("Menu")

BG= pygame.image.load('checkers/assets/Background.png')

def get_font(size):
    return pygame.font.Font('checkers/assets/font.ttf',size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(25).render("Este é o Play Screen.",True,"White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640,260))
        SCREEN.blit(PLAY_TEXT,PLAY_RECT)
        PLAY_BACK = Button(image=None, pos=(640, 460),text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def playerVsPlayer():
    from main import main
    main('PP')

def playVsMiniMax():
    from main import main
    main('PM')

def playVsAlphBeta():
    from main import main
    main('PA')

def CpuVsCpuMinimax():
    from main import main
    main('CM')

def CpuVsCpuAlphaBeta():
    from main import main
    main('CA')


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAYER_VS_PLAYER = Button(image=pygame.transform.scale(pygame.image.load("checkers/assets/Play Rect.png"),(600,90)), pos=(640, 250),text_input="PlayerVsPlayer", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        PLAYER_VS_MINIMAX = Button(image=pygame.transform.scale(pygame.image.load("checkers/assets/Play Rect.png"),(600,90)), pos=(640, 350),text_input="PlayVsMiniMax", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        PLAYER_VS_ALPHA_BETA = Button(image=pygame.transform.scale(pygame.image.load("checkers/assets/Play Rect.png"),(600,90)), pos=(640, 450),text_input="PlayVsAlphBeta", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        CPU_VS_CPU_MINIMAX = Button(image=pygame.transform.scale(pygame.image.load("checkers/assets/Play Rect.png"),(300,90)), pos=(640, 550),text_input="CpuVsCpu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        CPU_VS_CPU_APHA_BETA = Button(image=pygame.transform.scale(pygame.image.load("checkers/assets/Play Rect.png"),(300,90)), pos=(640, 650),text_input="CpuVsCpu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        # GAME_BUTTON = Button(image=pygame.image.load("checkers/assets/Options Rect.png"), pos=(640, 400), 
        #                      text_input="PLAY_PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        # QUIT_BUTTON = Button(image=pygame.image.load("checkers/assets/Quit Rect.png"), pos=(640, 550), 
        #                     text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAYER_VS_PLAYER,PLAYER_VS_MINIMAX,PLAYER_VS_ALPHA_BETA,CPU_VS_CPU_MINIMAX,CPU_VS_CPU_APHA_BETA]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_VS_PLAYER.checkForInput(MENU_MOUSE_POS):
                    playerVsPlayer()
                if PLAYER_VS_MINIMAX.checkForInput(MENU_MOUSE_POS):
                    playVsMiniMax()
                if PLAYER_VS_ALPHA_BETA.checkForInput(MENU_MOUSE_POS):
                    playVsAlphBeta()
                if CPU_VS_CPU_MINIMAX.checkForInput(MENU_MOUSE_POS):
                    CpuVsCpuMinimax()
                if CPU_VS_CPU_APHA_BETA.checkForInput(MENU_MOUSE_POS):
                    CpuVsCpuAlphaBeta()
                # if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     play()
                # if GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     playVsAlphBetaS()
                # if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     pygame.quit()
                #     sys.exit()

        pygame.display.update()

main_menu()
import pygame, sys
from buttons import Button

pygame.init()

SCREEN = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Начальное меню")


def get_font(size):
    return pygame.font.SysFont("times new roman", size)


def play():
    import os
    os.system('code.py')


def options():
    import os
    os.system('explore.py')


def main_menu():
    while True:
        SCREEN.fill((186, 230, 124))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(85).render("RECYCLE GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(420, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("data/rect6.png"), pos=(420, 210),
                             text_input="ИГРА", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("data/rect6.png"), pos=(420, 305),
                                text_input="УЧЕБНИК", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("data/rect6.png"), pos=(420, 400),
                             text_input="ВЫХОД", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
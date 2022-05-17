import os
import sys
import pygame
from buttons import Button


class BASA:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('thk1.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def get_font(size):
    return pygame.font.SysFont("times new roman", size)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('result')
    size = width, height = 850, 500
    screen = pygame.display.set_mode(size)
    #screen.fill(pygame.Color('white'))

    running = True
    mon = BASA()
    #screen.fill(pygame.Color('white'))
    while running:
        mon.draw(screen)
        QUIT_BUTTON = Button(image=pygame.image.load("data/rect8.png"), pos=(775, 30),
                             text_input="ВЫХОД", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        mouse_pos = pygame.mouse.get_pos()

        # for button in [QUIT_BUTTON]:
        #     button.changeColor(mouse_pos)
        #     button.update(screen)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         mouse_pos = event.pos
        #         # if QUIT_BUTTON.checkForInput(mouse_pos):
        #         #     running = False
        #         if QUIT_BUTTON.checkForInput(mouse_pos):
        #             pygame.quit()
        #             sys.exit()

        for button in [QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
    pygame.quit()
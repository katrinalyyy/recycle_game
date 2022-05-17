import pygame
import os
import sys



class BASA:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('учебник_2.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class SECOND:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('учебник2.png')

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


# class Ranger():
#     def __init__(self):
#         self.x = 30
#         self.y = 30
#         self.pos = self.x, self.y
#         self.image = load_image('ranger1.png')
#         objImageRect = self.image.get_rect()
#         self.img_rect = objImageRect
#
#     def draw(self, screen):
#         screen.blit(self.image, (self.x, self.y))
#
#
# class Instruct():
#     def __init__(self):
#         self.x = 160
#         self.y = 30
#         self.pos = self.x, self.y
#         self.image = load_image('instruct2.png')
#         objImageRect = self.image.get_rect()
#         self.img_rect = objImageRect
#
#     def draw(self, screen):
#         screen.blit(self.image, (self.x, self.y))
#
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('учебник')
#     size = width, height = 500, 500
#     screen = pygame.display.set_mode(size)
#
#     running = True
#     name = Ranger()
#     text = Instruct()
#     pygame.mouse.set_visible(False)
#     screen.fill(pygame.Color('white'))
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         name.draw(screen)
#         text.draw(screen)
#         pygame.display.flip()
#     pygame.quit()



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('учебник')
    size = width, height = 850, 500
    screen = pygame.display.set_mode(size)
    #screen.fill(pygame.Color('white'))

    running = True
    mon = BASA()
    mon2 = SECOND()
    # fps = 120
    # clock = pygame.time.Clock()
    #screen.fill(pygame.Color('white'))
    while running:
        mon.draw(screen)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #mon2.draw(screen)
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mon = mon2

        pygame.display.flip()
        # clock.tick(fps)
    pygame.quit()


    #     mouse_pos = pygame.mouse.get_pos()
    #     mon.draw(screen)
    #     pygame.display.flip()
    # pygame.quit()
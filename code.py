import os
import sys
from abc import ABC
from buttons import Button

import pygame
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # уч. чтоб избр сохранило прозрачность
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:  # если избр не прозрачное
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bak_blue(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('bak_blue2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def check_collision_with_object(self, object):
        if not object:
            return False
        if self.rect.colliderect(object.img_rect):
            return True
        return False


class Bak_yellow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('bak_yellow2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 300

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def check_collision_with_object(self, object):
        if not object:
            return False
        if self.rect.colliderect(object.img_rect):
            return True
        return False


class Bak_green(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('bak_green2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 460
        self.rect.y = 300

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def check_collision_with_object(self, object):
        if not object:
            return False
        if self.rect.colliderect(object.img_rect):
            return True
        return False


class Bak_red(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('bak_red2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 300

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def check_collision_with_object(self, object):
        if not object:
            return False
        if self.rect.colliderect(object.img_rect):
            return True
        return False


class AbstractBlueTrash(ABC):
    def __init__(self, filename):
        self.x = random.randrange(width - 300)
        self.y = random.randrange(height - 300)
        self.pos = self.x, self.y
        self.image = load_image(filename)
        objImageRect = self.image.get_rect()
        objImageRect.x = self.x
        objImageRect.y = self.y
        self.img_rect = objImageRect

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        if abs(mouse_pos[0] - self.img_rect.x) < self.img_rect.w and abs(
                mouse_pos[1] - self.img_rect.y) < self.img_rect.h:
            return True
        return False


class Trash_blue1(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue11.png')


class Trash_blue2(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue22.png')


class Trash_blue3(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue33.png')


class Trash_blue4(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue44.png')


class Trash_blue5(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue55.png')


class Trash_blue6(AbstractBlueTrash):
    def __init__(self):
        super().__init__('blue66.png')


class Trash_yellow1(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye1.png')


class Trash_yellow2(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye2.png')


class Trash_yellow3(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye3.png')


class Trash_yellow4(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye4.png')


class Trash_yellow5(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye5.png')


class Trash_yellow6(AbstractBlueTrash):
    def __init__(self):
        super().__init__('ye6.png')


class Trash_green1(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr1.png')


class Trash_green2(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr2.png')


class Trash_green3(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr3.png')


class Trash_green4(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr4.png')


class Trash_green5(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr5.png')


class Trash_green6(AbstractBlueTrash):
    def __init__(self):
        super().__init__('gr6.png')


class Trash_red1(AbstractBlueTrash):
    def __init__(self):
        super().__init__('rd1.png')


class Trash_red2(AbstractBlueTrash):
    def __init__(self):
        super().__init__('rd2.png')


def get_font(size):
    return pygame.font.SysFont("times new roman", size)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('recycle')
    size = width, height = 850, 500
    screen = pygame.display.set_mode(size)
    fps = 38

    running = True
    all_sprites = pygame.sprite.Group()
    bak_blue = Bak_blue(all_sprites)
    bak_yellow = Bak_yellow(all_sprites)
    bak_green = Bak_green(all_sprites)
    bak_red = Bak_red(all_sprites)

    tr_blue = [Trash_blue1(), Trash_blue2(), Trash_blue3(), Trash_blue4(), Trash_blue5(), Trash_blue6()]
    tr_yellow = [Trash_yellow1(), Trash_yellow2(), Trash_yellow3(), Trash_yellow4(), Trash_yellow5(), Trash_yellow6()]
    tr_green = [Trash_green1(), Trash_green2(), Trash_green3(), Trash_green4(), Trash_green5(), Trash_green6()]
    tr_red = [Trash_red1(), Trash_red2()]

    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    x2, y2 = 10, 10
    x1, y1 = 0, 0
    rect_x, rect_y = 0, 0
    screen.fill((252, 239, 230))
    selected_obj = None
    while running:
        QUIT_BUTTON = Button(image=pygame.image.load("data/rect8.png"), pos=(775, 30),
                             text_input="НАЗАД", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        mouse_pos = pygame.mouse.get_pos()

        for button in [QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    running = False
                for obj in tr_blue:
                    if obj:
                        if obj.is_clicked(mouse_pos):
                            selected_obj = obj
                for objt in tr_yellow:
                    if objt:
                        if objt.is_clicked(mouse_pos):
                            selected_obj = objt
                for objtt in tr_green:
                    if objtt:
                        if objtt.is_clicked(mouse_pos):
                            selected_obj = objtt
                for objte in tr_red:
                    if objte:
                        if objte.is_clicked(mouse_pos):
                            selected_obj = objte
            if event.type == pygame.MOUSEMOTION:
                if selected_obj:
                    new_mouse_pos = event.pos
                    selected_obj.x = new_mouse_pos[0]
                    selected_obj.y = new_mouse_pos[1]
                    selected_obj.img_rect.x = new_mouse_pos[0]
                    selected_obj.img_rect.y = new_mouse_pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                selected_obj = None

        for i in range(len(tr_blue)):
            if bak_blue.check_collision_with_object(tr_blue[i]):
                tr_blue[i] = None

        count_objects = 0
        for obj in tr_blue:
            if obj:
                count_objects += 1

        for obj in tr_blue:
            if obj:
                obj.draw(screen)

        for i in range(len(tr_yellow)):
            if bak_yellow.check_collision_with_object(tr_yellow[i]):
                tr_yellow[i] = None

        for obj in tr_yellow:
            if obj:
                count_objects += 1

        for obj in tr_yellow:
            if obj:
                obj.draw(screen)

        for i in range(len(tr_green)):
            if bak_green.check_collision_with_object(tr_green[i]):
                tr_green[i] = None

        for obj in tr_green:
            if obj:
                count_objects += 1

        for obj in tr_green:
            if obj:
                obj.draw(screen)
        pygame.display.flip()

        for i in range(len(tr_red)):
            if bak_red.check_collision_with_object(tr_red[i]):
                tr_red[i] = None

        for obj in tr_red:
            if obj:
                count_objects += 1

        clock.tick(fps)
        screen.fill((252, 239, 230))
        all_sprites.update()
        all_sprites.draw(screen)
        for obj in tr_red:
            if obj:
                obj.draw(screen)
        pygame.display.flip()

        if count_objects == 0:
            import os
            os.system('final.py')

    pygame.quit()
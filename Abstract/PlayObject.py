from abc import ABCMeta

import pygame


class PlayObject(metaclass=ABCMeta):
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))
        self.w, self.h = self.bitmap.get_size()

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

    def check_collision(self, ob):
        if self.y + self.h > ob.y and self.x + self.w > ob.x > self.x + self.w * 1 / 2:
            return True
        return False

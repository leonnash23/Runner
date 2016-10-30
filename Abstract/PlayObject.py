from abc import ABCMeta

import pygame


class PlayObject(metaclass=ABCMeta):
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

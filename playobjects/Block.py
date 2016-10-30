import pygame

from Abstract.PlayObject import PlayObject


class Block(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/block.png")
        self.speed = -0.5

    def move(self):
        self.x += self.speed
        w, h = self.bitmap.get_size()
        w += 1
        self.bitmap = pygame.transform.scale(self.bitmap, (w, h))

import pygame

from Abstract.PlayObject import PlayObject


class Block(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/block.png")
        self.speed = -0.5
        self.realspeed = -0.5
        self.visible = True

    def move(self):
        if self.x < 0:
            self.y += 40 / (50/abs(self.speed))
        self.x += self.realspeed
        w, h = self.bitmap.get_size()
        w += round(abs(self.speed)+0.5)
        self.bitmap = pygame.transform.scale(self.bitmap, (w, h))

    def reset(self):
        self.bitmap = pygame.transform.scale(self.bitmap, (self.w, self.h))
        self.x = 800
        self.y = 360
        self.realspeed = self.speed
        self.visible = True


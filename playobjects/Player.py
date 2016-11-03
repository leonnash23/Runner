import pygame

from Abstract.PlayObject import PlayObject
from Animator import Animator


class Player(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/player/1.png")
        bitmaps = [pygame.image.load("img/player/1.png"),
                   pygame.image.load("img/player/2.png"),
                   pygame.image.load("img/player/3.png")]
        bitmaps[0].set_colorkey((255, 255, 255))
        bitmaps[1].set_colorkey((255, 255, 255))
        bitmaps[2].set_colorkey((255, 255, 255))
        self.running_animator = Animator(bitmaps)
        self.points = 0
        self.up = False
        self.down = False
        self.speed = 0

    def jump(self):
        if self.y == 360:
            self.speed = -5
            self.up = True

    def move(self, dt):
        self.running_animator.update(dt)
        self.bitmap = self.running_animator.getImg()
        # ceiling
        if self.y <= 200:
            self.down = True
            self.up = False
        if self.down:
            self.speed = 3
        # floor
        if self.y >= 360 and self.down:
            self.y = 360
            self.down = False
            self.speed = 0
        self.y += self.speed

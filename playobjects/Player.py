import pygame

from Abstract.PlayObject import PlayObject


class Player(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/player.png")
        self.bitmaps = []
        self.bitmaps.append(pygame.image.load("img/player1.png"))
        self.bitmaps[0].set_colorkey((255, 255, 255))
        self.bitmaps.append(pygame.image.load("img/player.png"))
        self.bitmaps[1].set_colorkey((255, 255, 255))
        self.points = 0
        self.bitmap_id = 0
        self.up = False
        self.down = False
        self.speed = 0
        self.bitmap_tick = 0

    def jump(self):
        if self.y == 360:
            self.speed = -1.2
            self.up = True
            self.bitmap_id = 0

    def move(self):
        # ceiling
        if self.y <= 200:
            self.down = True
            self.up = False
        if self.down:
            self.speed = 0.8
        # floor
        if self.y >= 360 and self.down:
            self.y = 360
            self.down = False
            self.speed = 0
        self.y += self.speed
        if not self.up and not self.down and self.bitmap_tick >= 40:
            if self.bitmap_id == 0:
                self.bitmap_id = 1
            else:
                self.bitmap_id = 0
            self.bitmap_tick = 0
        self.bitmap = self.bitmaps[self.bitmap_id]
        self.bitmap_tick += 1

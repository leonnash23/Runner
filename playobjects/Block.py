import pygame

from Abstract.PlayObject import PlayObject


class Block(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/block.png")
        self.speed = -0.5
        self.speed_increase_step = -0.1
        self.real_speed = -0.5
        self.visible = True

    def move(self):
        # if x < 0 then block go down
        if self.x < 0:
            self.y += 40 / (50/abs(self.speed))
        self.x += self.real_speed
        w, h = self.bitmap.get_size()
        w += round(abs(self.speed)+0.5)
        self.bitmap = pygame.transform.scale(self.bitmap, (w, h))

    def reset(self):
        self.bitmap = pygame.transform.scale(self.bitmap, (self.w, self.h))
        self.x = 800
        self.y = 360
        self.real_speed = self.speed
        self.visible = True

    def increase_speed(self):
        self.speed += self.speed_increase_step


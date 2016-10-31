from Abstract.PlayObject import PlayObject


class Player(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/player.png")
        self.points = 0
        self.up = False
        self.down = False
        self.speed = 0

    def jump(self):
        if self.y == 360:
            self.speed = -1.2
            self.up = True

    def move(self):
        if self.y <= 200:
            self.down = True
            self.up = False
        if self.down:
            self.speed = 0.8
        if self.y >= 360 and self.down:
            self.y = 360
            self.down = False
            self.speed = 0
        self.y += self.speed

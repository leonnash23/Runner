from Abstract.PlayObject import PlayObject


class Player(PlayObject):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "img/player.png")
        self.points = 0
        self.up = False
        self.down = False

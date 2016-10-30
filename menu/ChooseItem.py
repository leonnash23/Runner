from Abstract.Buttons import Buttons
from menu.Item import Item


class ChooseItem(Item):
    def __init__(self, text, x, y, b: Buttons):
        super().__init__(text, x, y)
        self.chosen = False
        self.color = (58, 170, 207)
        self.type = b

    def check_click(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.notify_all(x, y, self.type)

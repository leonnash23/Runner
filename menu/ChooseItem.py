from Abstract.Buttons import Buttons
from Abstract.ObservableButton import ObservableButton
from menu.Item import Item


class ChooseItem(Item):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.chosen = False
        self.color = (58, 170, 207)
        self.type = Buttons.Start

    def check_click(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.notify_all(x, y, self.type)

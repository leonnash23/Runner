from menu.Item import Item


class ChooseItem(Item):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.chosen = False
        self.color = (58, 170, 207)

import pygame

from Abstract.ObservableButton import ObservableButton


class Item(ObservableButton):
    def __init__(self, text, x, y):
        super().__init__()
        pygame.font.init()
        self.text = text
        self.font = pygame.font.Font("fonts/Mono.ttf", 32)
        self.x = x / 2 - self.font.size(text)[0] / 2
        self.y = y
        self.width = self.font.size(text)[0]
        self.height = self.font.size(text)[1]
        self.color = (255, 13, 0)

    def render(self, menu_screen):
        menu_screen.blit(self.font.render(self.text, 1, self.color), (self.x, self.y))

    def check_click(self, x, y):
        pass

    def check_mouseovers(self, x, y):
        pass

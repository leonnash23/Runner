import pygame
import sys

from menu.Item import Item


class Menu:
    def __init__(self, w, h, items):
        self.items = []
        for i in items:
            self.items.append(i)
        if len(self.items) == 0:
            self.items.append(Item("Старт", w, h / 2 - 30))
        else:
            self.items.append(Item("Старт", w, h / 2 - 30+self.items[-1].height+30))

        self.menu_screen = pygame.Surface((w, h))
        self.done = True

    def render(self):
        for i in self.items:
            self.menu_screen.blit(i.font.render(i.text, 1, i.color), (i.x, i.y))

    def check_items(self, x, y):
        for i in self.items:
            if i.x <= x <= i.x+i.width and i.y <= y <= i.y+i.height:
                if i.text == "Старт":
                    self.done = False

    def menu(self, parent):
        pygame.key.set_repeat(0, 0)
        while self.done:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    pos = pygame.mouse.get_pos()
                    self.check_items(pos[0], pos[1])

            self.menu_screen.fill((255, 255, 255))
            self.render()
            parent.blit(self.menu_screen, (0, 0))
            pygame.display.flip()

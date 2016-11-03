import sys

import pygame

from Abstract.Buttons import Buttons
from Abstract.ButtonsListener import ButtonsListener
from menu.ChooseItem import ChooseItem
from menu.Item import Item


class Menu(ButtonsListener):
    def update(self, x, y, b: Buttons):
        if b == Buttons.Start:
            self.done = False
        elif b == Buttons.Quit:
            sys.exit(0)

    def __init__(self, w, h, items):
        self.items = []
        for i in items:
            self.items.append(i)
        self.add_item(ChooseItem("Старт", w, h / 2 - 30, Buttons.Start))
        self.add_item(ChooseItem("Выход", w, h / 2 - 30, Buttons.Quit))
        self.menu_screen = pygame.Surface((w, h))
        self.done = True

    def render(self):
        for i in self.items:
            i.render(self.menu_screen)

    def check_items_click(self, x, y):
        for i in self.items:
            i.check_click(x, y)

    def check_items_mouseovers(self, x, y):
        for i in self.items:
            i.check_mouseovers(x, y)

    def menu(self, parent):
        time_delay = pygame.time.Clock()
        pygame.key.set_repeat(0, 0)
        while self.done:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    pos = pygame.mouse.get_pos()
                    self.check_items_click(pos[0], pos[1])
                if e.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.check_items_mouseovers(pos[0], pos[1])

            self.menu_screen.fill((255, 255, 255))
            self.render()
            parent.blit(self.menu_screen, (0, 0))
            pygame.display.flip()
            time_delay.tick(40)
        pygame.key.set_repeat(1, 1)

    def add_item(self, item: Item):
        item.register(self)
        if len(self.items) == 0:
            self.items.append(item)
        else:
            item.y = self.items[-1].y + self.items[-1].height + 15
            self.items.append(item)

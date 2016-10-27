import pygame


class Item:
    def __init__(self, text,x,y):
        pygame.font.init()
        self.text = text
        self.font = pygame.font.Font("fonts/Mono.ttf", 32)
        self.x = x/2-self.font.size(text)[0]/2
        self.y = y
        self.width = self.font.size(text)[0]
        self.height = self.font.size(text)[1]
        self.chosen = False
        self.color = (58, 170, 207)


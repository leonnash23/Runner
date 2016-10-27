import random

import pygame

from menu.Item import Item
from menu.Menu import Menu

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RUN!")

screen = pygame.Surface((800, 400))

x = 0
y = 0
square_go_right = True
square_go_down = True


class Player:
    def __init__(self, xpos, ypos):
        self.points = 0
        self.x = xpos
        self.y = ypos
        self.up = False
        self.down = False
        self.bitmap = pygame.image.load("img/player.png")
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Block:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.speed = -0.5
        self.bitmap = pygame.image.load("img/block.png")
        self.bitmap.set_colorkey((255, 255, 255))

    def move(self):
        self.x += self.speed
        w, h = self.bitmap.get_size()
        w += 1
        self.bitmap = pygame.transform.scale(self.bitmap, (w, h))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


w, h = pygame.display.get_surface().get_size()

menu = Menu(w, h, [])
menu.menu(window)

player = Player(0, 360)
block = Block(800, 360)
pygame.font.init()
font = pygame.font.Font("fonts/Mono.ttf", 32)

done = True
pygame.key.set_repeat(1, 1)

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and player.y == 360:
                player.up = True
        if e.type == pygame.KEYUP:
            player.up = False
    screen.fill((255, 255, 255))

    # render
    player.render()
    f = font.render("points %d" % player.points, 1, (0, 0, 0))
    screen.blit(f, (0, 0))
    if block is not None:
        block.render()
    window.blit(screen, (0, 0))

    # Player logic
    if player.y < 360 and not player.up or player.down:
        player.y += 0.8
    elif player.y > 200 and player.up:
        player.y -= 1.2
    if player.y >= 360:
        player.y = 360
        player.down = False
    if player.y <= 200:
        player.down = True

    # Block logic

    if block is not None:
        block.move()
        if block.x < 0:
            block.y += 4 / 5
        if block.x < -50:
            del block
            block = None
            player.points += 1

    if block is None:
        if random.randint(0, 10000) > 9990:
            block = Block(800, 360)

    # Relation logic
    if block is not None:
        if player.y + 40 > block.y and player.x + 40 > block.x > player.x + 30:
            menu = Menu(w, h, [])
            menu.menu(window)
            block = Block(800, 360)
            player = Player(0, 360)

        if block.x < player.x + 30 and player.y > block.y:
            player.y = block.y

    pygame.display.flip()

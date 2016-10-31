import random

import pygame

from menu.Item import Item
from menu.Menu import Menu
from playobjects.Block import Block
from playobjects.Player import Player

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RUN!")

screen = pygame.Surface((800, 400))

x = 0
y = 0
square_go_right = True
square_go_down = True

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
            if e.key == pygame.K_SPACE:
                player.jump()
    screen.fill((255, 255, 255))

    # render
    player.render(screen)
    f = font.render("points %d" % player.points, 1, (0, 0, 0))
    screen.blit(f, (0, 0))
    if block is not None:
        block.render(screen)
    window.blit(screen, (0, 0))

    # Relation logic
    if block.visible:
        if player.check_collision(block):
            menu = Menu(w, h, [Item("Points = %d" % player.points, w, h / 2)])
            menu.menu(window)
            block = Block(800, 360)
            player = Player(0, 360)
        if block.x < player.x + 40 and player.y + player.h > block.y:
            player.y = min(360, block.y-40)

    player.move()

    # Block logic

    if block.visible:
        block.move()
        if block.x < -50:
            block.y = 400
            block.visible = False
            block.real_speed = 0
            player.points += 1
            if player.points % 5 == 0:
                block.increase_speed()

    if not block.visible:
        if random.randint(0, 10000) > 9990:
            block.reset()

    pygame.display.flip()

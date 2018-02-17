import pygame, sys, random
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

world = []

x = random.randrange(0, width)
y = random.randrange(0, height)

loc = [x, y]

ball = pygame.image.load("assets/ball.gif")
ballrect = ball.get_rect()
ballrect = ballrect.move(loc)
world.append(ballrect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    for ballrect in world:
        ballrect = world.pop()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        world.append(ballrect)
        screen.blit(ball, ballrect)

    pygame.display.flip()



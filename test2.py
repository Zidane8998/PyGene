WINDOW_TITLE = "Pygame Genetic Algorithm Test"

import pygame
from pygame.locals import *

import random
import math


class Ball():
    def __init__(self, ball, vector):
        self.x = 1
        self.y = 1
        self.vector = vector
        self.speed = None
        self.iterations = 1000
        self.random_direction = random.randrange(0, 2)

        #generate random coordinates here
        randX = random.randrange(0, 800)
        randY = random.randrange(0, 600)
        #check that random location isn't close to bounds
        while randX > 600 or randX < 100:
            randX = random.randrange(0, 800)
        while randY > 400 or randY < 100:
            randY = random.randrange(0, 600)

        self.location = [randX, randY]
        self.ballrect = ball.get_rect()
        self.initMove(self.location)

    def setSpeed(self, x, y):
        """
        if x > 1:
            x = 1
            y = 1
        if y > 1:
            x = 1
            y = 1
        """
        self.x += x
        self.y += y
        self.speed = [self.x, self.y]


    def move(self):
        #decompose angle and speed
        (angle, z) = self.vector

        #add random movement
        #add or subtract a scalar value to only one axis per 1000 iterations
        tmp = random.random() * 0.2
        op = random.randrange(0, 2)

        if op == 0 and self.random_direction == 0:
            angle += tmp
        elif op == 1 and self.random_direction == 0:
            angle -= tmp
        if op == 0 and self.random_direction == 1:
            angle += tmp
        elif op == 1 and self.random_direction == 1:
            angle -= tmp

        #if the new coordinates cause a bump against the wall, change direction
        if self.ballrect.left < 0 or self.ballrect.right > 800:
            angle *= -1
        if self.ballrect.top < 0 or self.ballrect.bottom > 600:
            z *= -1

        #re-compose angle and speed
        self.vector = (angle, z)

        #update the rectangle
        self.speed = self.calcnewpos()
        self.ballrect = self.ballrect.move(self.vector)

        #update the iteration counter for smooth random movement and reset the random direction flag
        self.iterations -= 1
        if self.iterations <= 0:
            self.iterations = 1000
            self.random_direction = random.randrange(0, 2)

    def calcnewpos(self):
            (angle, z) = self.vector
            (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
            return dx, dy

    def initMove(self, loc):
        self.ballrect = self.ballrect.move(loc)

    def draw(self, ball, screen):
        screen.blit(ball, self.ballrect)

    def update(self):
        self.move()


class GameWorld():
    def __init__(self):
        self.world = []
        self.ball = pygame.image.load("ball.gif")

        for i in range(0, 1):
            b = Ball(self.ball, (1, 1))
            self.world.append(b)

        print "GameWorld: initialized"

    def update(self):
        for ballrect in self.world:
            ballrect.update()

    def draw(self, screen):
        for ballrect in self.world:
            ballrect.draw(self.ball, screen)


class GameMain():
    """game Main. entry point. handles initialization of game and graphics, as well as game loop."""
    done = False
    color_bg = Color('darkgrey') # or also: Color(50,50,50) , or: Color('#fefefe')

    def __init__(self, width=800, height=600):
        """Initialize PyGame window.

        variables:
            width, height = screen width, height
            screen = main video surface, to draw on

            fps_max = framerate limit to the max fps
            limit_fps = boolean toggles capping FPS, to share cpu, or let it run free.
            now = current time in Milliseconds. ( 1000ms = 1second)
        """
        pygame.init()

        self.GameWorld = GameWorld()
        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode(( self.width, self.height ))
        pygame.display.set_caption( WINDOW_TITLE )

        # fps clock, limits max fps
        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.fps_max = 100

    def main_loop(self):
        """Game() main loop."""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            # cap FPS if: limit_fps == True
            if self.limit_fps: self.clock.tick( self.fps_max )
            else: self.clock.tick()

    def draw(self):

        self.screen.fill( self.color_bg )

        # draw your stuff here. sprites, gui, etc....
        self.GameWorld.draw(self.screen)
        pygame.display.flip()

    def update(self):

        self.now = pygame.time.get_ticks()
        self.GameWorld.update()

    def handle_events(self):

        events = pygame.event.get()
        kmods = pygame.key.get_mods()

        for event in events:
            if event.type == pygame.QUIT: self.done = True
            # event: keydown
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: self.done = True

if __name__ == "__main__":
    game = GameMain()
    game.main_loop()


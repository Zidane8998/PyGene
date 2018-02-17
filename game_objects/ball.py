import random
import math


class Ball:
    def __init__(self, ball, vector):
        self.x = 1
        self.y = 1
        self.vector = vector
        self.speed = None
        self.iterations = 1000
        self.random_direction = random.randrange(0, 2)

        # generate random coordinates here

        randX = random.randrange(0, 800)
        randY = random.randrange(0, 600)

        # check that random location isn't close to bounds

        while randX > 600 or randX < 100:
            randX = random.randrange(0, 800)
        while randY > 400 or randY < 100:
            randY = random.randrange(0, 600)

        self.location = [randX, randY]
        self.ballrect = ball.get_rect()
        self.initmove(self.location)

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
        # decompose angle and speed
        (angle, z) = self.vector

        # add random movement
        # add or subtract a scalar value to only one axis per 1000 iterations
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

        # if the new coordinates cause a bump against the wall, change direction
        if self.ballrect.left < 0 or self.ballrect.right > 800:
            angle *= -1
        if self.ballrect.top < 0 or self.ballrect.bottom > 600:
            z *= -1

        # re-compose angle and speed
        self.vector = (angle, z)

        # update the rectangle
        self.speed = self.calcnewpos()
        self.ballrect = self.ballrect.move(self.vector)

        # update the iteration counter for smooth random movement and reset the random direction flag
        self.iterations -= 1
        if self.iterations <= 0:
            self.iterations = 1000
            self.random_direction = random.randrange(0, 2)

    def calcnewpos(self):
            (angle, z) = self.vector
            (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
            return dx, dy

    def initmove(self, loc):
        self.ballrect = self.ballrect.move(loc)

    def draw(self, ball, screen):
        screen.blit(ball, self.ballrect)

    def update(self):
        self.move()
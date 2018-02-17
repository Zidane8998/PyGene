import pygame
import os
from game_objects.ball import Ball
import constants


class GameWorld:
    def __init__(self):
        self.world = []
        self.constants = constants.Constants()
        self.ball = pygame.image.load(os.path.join(self.constants.assets_dir, "ball.gif"))

        for i in range(0, 2):
            b = Ball(self.ball, (1, 1))
            self.world.append(b)

        print("GameWorld: initialized")

    def update(self):
        for ball in self.world:
            ball.update()

    def draw(self, screen):
        for ball in self.world:
            ball.draw(self.ball, screen)

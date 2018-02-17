import pygame
from pygame.locals import *

from game_objects.gameworld import GameWorld

WINDOW_TITLE = "Pygame Genetic Algorithm Test"


class GameMain:
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
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 0)
        pygame.display.set_caption(WINDOW_TITLE)

        # fps clock, limits max fps
        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.fps_max = 100
        self.now = None

    def main_loop(self):
        """Game() main loop."""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            # cap FPS if: limit_fps == True
            if self.limit_fps:
                self.clock.tick( self.fps_max )
            else:
                self.clock.tick()

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
            if event.type == pygame.QUIT:
                self.done = True
            # event: keydown
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
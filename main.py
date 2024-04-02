import pygame
import sys

# Scripts will be loaded here
from scripts.gamestate import GameStateManager
from scripts.menu import Start
from scripts.game import Level

# Game setting and variable
screen_width = 992
screen_height = 544
game_fps = 60

# Game class
class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Set the window caption and display size
        pygame.display.set_caption("Game")
        # Set the game screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Set the game display size
        self.display = pygame.Surface((screen_width / 2, screen_height / 2))
        # Set the game clock
        self.clock = pygame.time.Clock()

        # Set and config Game Scenes
        self.gameStateManager = GameStateManager('start_scene')
        self.start = Start(self.gameStateManager)
        self.level = Level(self.gameStateManager)
        self.states = {
            'start_scene': self.start,
            'level_scene': self.level,
        }

    # Main game loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Running Scene
            self.states[self.gameStateManager.get_state()].run()

            # Update the Display
            pygame.display.update()
            # Game FPS
            self.clock.tick(game_fps)

if __name__ == '__main__':
    game = Game()
    game.run()
import pygame
import sys

# Scripts will be loaded here
from scripts.utils import load_round_letter_images, load_background_images

# Game window setting
display_width = 800
display_height = 600

# Game class
class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Set the window caption and display size
        pygame.display.set_caption("Game")
        # Set the game display size
        self.screen = pygame.display.set_mode((display_width, display_height))
        # Set the game clock
        self.clock = pygame.time.Clock()

        # Assets will be loaded here
        self.assets = {
            'round_letter_images': load_round_letter_images(),
            'background_images': load_background_images(),
        }

    # Main game loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Game logic goes here
            pygame.display.update()
            self.clock.tick(60)

Game().run()
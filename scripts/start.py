import pygame

# Scripts will be loaded here
from scripts.utils import load_image
from scripts.menubutton import Button

# Game setting and variable
screen_width = 992
screen_height = 544
game_fps = 60

# Start class aka start menu
class Start:
    def __init__(self, gameStateManager):
        # Set the game screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Set the game display size
        self.display = pygame.Surface((screen_width / 2, screen_height / 2))
        # Set the game scene manager
        self.gameStateManager = gameStateManager

        # Assets will be loaded here
        self.assets = {
            'background2': load_image('/background2.png'),
            'startbtn': load_image('/Buttons/Rect/PlayText/Default.png'),
        }

        self.startbtn = Button(screen_width / 2 - 70, screen_height / 2 - 70, self.assets['startbtn'], 1, self.gameStateManager)

    def run(self):
        # Background
        self.screen.blit(self.assets['background2'], (0, 0))
        # Start Button
        self.startbtn.draw(self.screen)
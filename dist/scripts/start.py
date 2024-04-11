import pygame

# Scripts will be loaded here
from scripts.utils import load_image, load_images
from scripts.menubutton import Button
from scripts.background import backgrounds

# Game setting and variable
screen_width = 992
screen_height = 600

# Start class aka start menu
class Start:
    def __init__(self, gameStateManager):
        # Initialize pygame
        pygame.init()
        # Set the game screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Set the game display size
        self.display = pygame.Surface((screen_width / 2, screen_height / 2))
        # Set the game scene manager
        self.gameStateManager = gameStateManager

        # Assets will be loaded here
        self.assets = {
            'startbtn': load_image('/Buttons/Rect/PlayText/Default.png'),
            'background': load_image('/background.png'),
            'bg_clouds': load_images('/bg_elements/clouds'),
        }
        # Background clouds create
        self.bg_clouds = backgrounds(self.assets['bg_clouds'], count=16)
        # XY
        self.scroll = [0, 0]

        # Start Button
        self.startbtn = Button(screen_width / 2 - 70, screen_height / 2 - 70, self.assets['startbtn'], 1, self.gameStateManager)

    def run(self):
        # Background image
        self.display.blit(self.assets['background'], (0, 0))

        # Camera Render Scrolling for xy coord
        self.scroll[0] = self.display.get_width() / 2
        self.scroll[1] = self.display.get_height() / 2
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

        # Background Elements
        self.bg_clouds.update()
        self.bg_clouds.render(self.display, offset=render_scroll)

        # Transform the display to screen
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        # Start Button
        self.startbtn.draw(self.screen)
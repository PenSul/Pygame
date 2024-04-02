import pygame

# Scripts will be loaded here
from scripts.utils import load_image, load_images
from scripts.background import backgrounds

# Game setting and variable
screen_width = 992
screen_height = 544
game_fps = 60

# GamePlay class
class Level:
    def __init__(self, gameStateManager):
        # Set the game screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Set the game display size
        self.display = pygame.Surface((screen_width / 2, screen_height / 2))
        # Set the game scene manager
        self.gameStateManager = gameStateManager

        # Assets will be loaded here
        self.assets = {
            'round_letters': load_images('/round_letters'),
            'background': load_image('/background.png'),
            'bg_clouds': load_images('/bg_elements/clouds'),
        }

        # Background clouds create
        self.bg_clouds = backgrounds(self.assets['bg_clouds'], count=16)

        self.scroll = [0, 0]

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

        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
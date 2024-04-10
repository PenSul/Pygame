'''Pygame/Background Tests'''

# Python module(s)
import pygame
import os
import sys
import unittest

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.background import background, backgrounds

# Game setting and variable
screen_width = 992
screen_height = 544

# Test case for background image building, updating and rendering
class TestBackground(unittest.TestCase):
    def setUp(self):
        self.image = pygame.Surface((100, 100))
        self.background = background([0, 0], self.image, 1, 1)

    def test_update(self):
        initial_pos = self.background.pos.copy()
        self.background.update()
        self.assertEqual(self.background.pos[0], initial_pos[0] + self.background.speed)

    def test_render(self):
        surf = pygame.Surface((screen_width, screen_height))
        offset = (0, 0)
        self.background.render(surf, offset)

# Test case for background image(s) building, updating and rendering
class TestBackgrounds(unittest.TestCase):
    def setUp(self):
        self.images = [pygame.Surface((100, 100)) for _ in range(3)]
        self.backgrounds = backgrounds(self.images, 3)

    def test_update(self):
        for background in self.backgrounds.background_images:
            initial_pos = background.pos.copy()
            background.update()
            self.assertEqual(background.pos[0], initial_pos[0] + background.speed)

    def test_render(self):
        surf = pygame.Surface((screen_width, screen_height))
        offset = (0, 0)
        self.backgrounds.render(surf, offset)

if __name__ == '__main__':
    unittest.main()
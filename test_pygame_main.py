'''Pygame/GUI Tests'''

# Python Module(s)
import sys
import os
import pygame
import unittest

# Add the root directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import the GameStateManager and Game classes for testing
from scripts.gamestate import GameStateManager
from main import Game

# Define a test class TestGame that inherits from unittest.TestCase
class TestGame(unittest.TestCase):
    # Define a test method test_game_initialization to test the initialization of the Game class
    def test_game_initialization(self):
        # Instantiate the Game class
        game = Game()
        # Assert that the screen attribute is an instance of pygame Surface
        self.assertIsInstance(game.screen, pygame.Surface, "Fail to create screen")
        # Assert that the display attribute is an instance of pygame Surface
        self.assertIsInstance(game.display, pygame.Surface, "fail to create display")
        # Assert that the clock attribute is an instance of pygame time Clock
        self.assertIsInstance(game.clock, pygame.time.Clock, "Fail to adjust to clock speed")
        # Assert that the gameStateManager attribute is an instance of GameStateManager
        self.assertIsInstance(game.gameStateManager, GameStateManager, "Fail to load game scene manager")
        # Assert that the initial state of the game is 'start_scene'
        self.assertEqual(game.gameStateManager.get_state(), 'start_scene', "Fail to load start_scene")

# Run the unit tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
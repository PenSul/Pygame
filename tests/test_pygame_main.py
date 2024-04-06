'''Pygame/GUI Tests'''

# Python module(s)
import sys
import os
import pygame
import unittest

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Scripts will be loaded here
from scripts.gamestate import GameStateManager
from main import Game

# Test Cases of Game Initialization
class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game()
        self.assertIsInstance(game.screen, pygame.Surface)
        self.assertIsInstance(game.display, pygame.Surface)
        self.assertIsInstance(game.clock, pygame.time.Clock)
        self.assertIsInstance(game.gameStateManager, GameStateManager)
        self.assertEqual(game.gameStateManager.get_state(), 'start_scene')

if __name__ == '__main__':
    unittest.main()
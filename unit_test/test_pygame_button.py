'''Pygame/Button Tests'''

# Python module(s)
import pygame
import os
import sys
import unittest
from unittest.mock import Mock, patch

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.menubutton import Button

# Test case of Button from different scenes (this focus on startbtn)
class TestMenuButton(unittest.TestCase):
    @patch('pygame.mouse.get_pos', return_value=(50, 50))
    @patch('pygame.mouse.get_pressed', return_value=(0, 0, 0))
    def test_draw(self, mock_get_pressed, mock_get_pos):
        surf = Mock()
        button = Button(0, 0, pygame.Surface((100, 100)), 1, Mock())

        # Call the draw method and check the return value
        self.assertFalse(button.draw(surf))  # No action expected
        
        # Check if the button image is set correctly when not hovered
        self.assertEqual(button.image.get_width(), button.assets['startbtn'].get_width())
        self.assertEqual(button.image.get_colorkey(), button.assets['startbtn'].get_colorkey())
        
        # Simulate hovering over the button
        button.rect.topleft = (0, 0)  # Move button to mouse position for hover effect
        button.draw(surf)  # Call draw method again after hovering
        
        # Check if the button image is set correctly when hovered
        self.assertEqual(button.image.get_width(), button.assets['startbtnhover'].get_width())
        self.assertEqual(button.image.get_colorkey(), button.assets['startbtnhover'].get_colorkey())
        
        # Check if action is triggered when button is clicked
        mock_get_pressed.return_value = (1, 0, 0)  # Simulate mouse click
        self.assertTrue(button.draw(surf))  # Action expected

if __name__ == '__main__':
    unittest.main()
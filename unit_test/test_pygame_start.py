'''Pygame/Start Tests'''

# Python Module(s)
import sys
import os
import unittest
from unittest.mock import patch, Mock

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.start import Start

class TestStart(unittest.TestCase):
    @patch('pygame.display.set_mode')
    @patch('pygame.Surface')
    @patch('pygame.display.set_mode')
    def setUp(self, mock_set_mode, mock_surface, mock_display):
        self.start = Start(Mock())

    def test_run(self):
        with patch('pygame.display.set_mode'):
            with patch('pygame.transform.scale'):
                self.start.run()
                self.assertIsNotNone(self.start.display)
                self.assertTrue('startbtn' in self.start.assets)
                self.assertTrue('background' in self.start.assets)
                self.assertTrue('bg_clouds' in self.start.assets)
                self.assertIsNotNone(self.start.bg_clouds)
                self.assertIsNotNone(self.start.startbtn)

if __name__ == '__main__':
    unittest.main()
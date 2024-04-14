'''Pygame/Start Tests'''

# Python Module(s)
import sys
import os
import unittest
from unittest.mock import patch, Mock

# Add the root directory to the Python path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import the Start class from the scripts module for testing
from scripts.start import Start

# Define a test class TestStart that inherits from unittest.TestCase
class TestStart(unittest.TestCase):
    # Set up the test environment before running each test case
    @patch('pygame.display.set_mode')
    @patch('pygame.Surface')
    @patch('pygame.display.set_mode')
    def setUp(self, mock_set_mode, mock_surface, mock_display):
        # Instantiate the Start class with a Mock object for testing
        self.start = Start(Mock())
    # Define a test method test_run to test the run method of the Start class
    def test_run(self):
        # Patch pygame display set mode for testing
        with patch('pygame.display.set_mode'):
            # Patch pygame transform scale for testing
            with patch('pygame.transform.scale'):
                # Call the run method of the Start class
                self.start.run()
                # Assert that the display attribute is not None after running
                self.assertIsNotNone(self.start.display)
                # Assert that 'startbtn' asset is present in the assets dictionary
                self.assertTrue('startbtn' in self.start.assets)
                # Assert that 'background' asset is present in the assets dictionary
                self.assertTrue('background' in self.start.assets)
                # Assert that 'bg_clouds' asset is present in the assets dictionary
                self.assertTrue('bg_clouds' in self.start.assets)
                # Assert that the bg_clouds attribute is not None after running
                self.assertIsNotNone(self.start.bg_clouds)
                # Assert that the startbtn attribute is not None after running
                self.assertIsNotNone(self.start.startbtn)

# Run the unit tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
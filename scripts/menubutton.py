import pygame
import os
import sys

# Scripts will be loaded here
from scripts.utils import load_image, outline

current_dir = os.path.dirname(os.path.abspath(__file__))
board_path = os.path.join(current_dir, "board.py")

# Game setting and variable
screen_width = 1000
screen_height = 600

# Button class
class Button:
	def __init__(self, x, y, image, scale, gameStateManager):
		# Initialize pygame
		pygame.init()
		# Set the game screen size
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		# Set the game display size
		self.display = pygame.Surface((screen_width / 2, screen_height / 2))

		# Button Variables
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.gameStateManager = gameStateManager

		# Assets will be loaded here
		self.assets = {
			'startbtn': load_image('/Buttons/Rect/PlayText/Default.png'),
            'startbtnhover': load_image('/Buttons/Rect/PlayText/Hover.png')
        }

	# Draw function to display the button on the screen
	def draw(self, surf):
		action = False  # Initialize the action variable to False

		# Get the current mouse position
		pos = pygame.mouse.get_pos()

		# Check if the mouse is over the button and if it is clicked
		if self.rect.collidepoint(pos):
			self.image = self.assets['startbtnhover']  # Change the button image to the hover state
			outline(self.image, (self.rect.topleft))  # Outline the button image with white line when hover
			if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:  # Check if the left mouse button is clicked
				self.clicked = True  # Set the clicked flag to True
				action = True  # Set the action variable to True
				pygame.quit()
				os.system("python " + board_path)  # Execute the board script if the game state is 'start_scene'
				sys.exit()
				
		else:
			self.image = self.assets['startbtn']  # Set the button image back to the default state

		if pygame.mouse.get_pressed()[0] == 0:  # Check if the left mouse button is released
			self.clicked = False  # Reset the clicked flag to False

		# Draw the button on the screen
		surf.blit(self.image, (self.rect.x, self.rect.y))

		return action  # Return the value of the action variable
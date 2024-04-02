import pygame

# Button class
class Button:
	def __init__(self, x, y, image, scale, gameStateManager):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.gameStateManager = gameStateManager

	def draw(self, surf):
		action = False
		# Get mouse position
		pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
				if self.gameStateManager.get_state() == 'start_scene':
					self.gameStateManager.set_state('level_scene')

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# Draw button on screen
		surf.blit(self.image, (self.rect.x, self.rect.y))

		return action
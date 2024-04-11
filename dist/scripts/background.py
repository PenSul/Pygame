# Python Module(s)
import random

# Single background class
class background:
    # Initialize the background object with position, image, speed, and depth
    def __init__(self, pos, image, speed, depth):
        # Store the position as a list
        self.pos = list(pos)
        # Store the image to be rendered
        self.image = image
        # Store the speed at which the background moves
        self.speed = speed
        # Store the depth for parallax effect
        self.depth = depth

    # Update the position of the background based on its speed
    def update(self):
        self.pos[0] += self.speed

    # Render the background with a parallax effect
    def render(self, surf, offset=(0, 0)):
        # Calculate the position to render the background with parallax effect
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)

        # Ensure the background stays within bounds and render it properly
        surf.blit(self.image, (render_pos[0] % (surf.get_width() + self.image.get_width()) - self.image.get_width(), render_pos[1] % (surf.get_height() + self.image.get_height()) - self.image.get_height()))

# Collection of multiple background objects
class backgrounds:
    # Initialize the backgrounds with a list of images and count of backgrounds
    def __init__(self, images, count):
        # Initialize an empty list to store background objects
        self.background_images = []

        # Create 'count' number of background objects with random properties
        for i in range(count):
            self.background_images.append(background((random.random() * 99999, random.random() * 99999), random.choice(images), random.random() * 0.06 + 0.06, random.random() * 0.61 + 0.21))

        # Sort the background objects based on depth for proper rendering order
        self.background_images.sort(key=lambda x: x.depth)

    # Update all background objects in the collection
    def update(self):
        # Call the update method for each background
        for background in self.background_images:
            background.update()

    # Render all background objects in the collection
    def render(self, surf, offset=(0, 0)):
        # Call the render method for each background
        for background in self.background_images:
            background.render(surf, offset)
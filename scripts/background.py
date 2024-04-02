import random

class background:
    def __init__(self, pos, image, speed, depth):
        self.pos = list(pos)
        self.image = image
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset=(0, 0)):
        # Parallex effect
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)

        # Ensure the background doesn't go out of bounds and show inproperly
        surf.blit(self.image, (render_pos[0] % (surf.get_width() + self.image.get_width()) - self.image.get_width(), render_pos[1] % (surf.get_height() + self.image.get_height()) - self.image.get_height()))

class backgrounds:
    def __init__(self, images, count):
        self.background_images = []

        for i in range(count):
            self.background_images.append(background((random.random() * 99999, random.random() * 99999), random.choice(images), random.random() * 0.06 + 0.06, random.random() * 0.61 + 0.21))

        # This tell how the images can be sorted
        self.background_images.sort(key=lambda x: x.depth)

    def update(self):
        for background in self.background_images:
            background.update()

    def render(self, surf, offset=(0, 0)):
        for background in self.background_images:
            background.render(surf, offset)
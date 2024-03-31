import pygame
import os

BASE_IMG_PATH = 'assets/images'

# Load images path
def load_image(path):
    image = pygame.image.load(path).convert_alpha()
    return image

# Load round letter images
def load_round_letter_images():
    round_letter_images = {}
    for letter in range(ord('a'), ord('z') + 1):
        letter_path = os.path.join(BASE_IMG_PATH, 'round_letters', chr(letter) + '.png')
        image = load_image(letter_path)
        round_letter_images[chr(letter)] = image
    return round_letter_images

# Load background images
def load_background_images():
    background_images = {}
    background_path = os.path.join(BASE_IMG_PATH, 'background', 'cake_valley_layers')

    for filename in os.listdir(background_path):
        if filename.endswith('.png'):
            image_path = os.path.join(background_path, filename)
            image = load_image(image_path)
            image_name = os.path.splitext(filename)[0]
            background_images[image_name] = image

    return background_images

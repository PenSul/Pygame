import pygame
import os

BASE_IMG_PATH = 'assets/images'

# Load image path
def load_image(path):
    image = pygame.image.load(BASE_IMG_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    return image

# Load images path
def load_images(path):
    images = []
    for images_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + images_name))
    return images
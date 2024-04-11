import pygame
import os

pygame.init()

# Game setting and variable
screen_width = 992
screen_height = 600

# Set the game screen size
screen = pygame.display.set_mode((screen_width, screen_height))
# Set the game display size
display = pygame.Surface((screen_width / 2, screen_height / 2))

BASE_IMG_PATH = 'assets/images'

# Load image path
def load_image(path):
    image = pygame.image.load(BASE_IMG_PATH + path)
    image.set_colorkey((0, 0, 0))
    return image

# Load images path
def load_images(path):
    images = []
    for images_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + images_name))
    return images

def outline(img, loc):
    mask = pygame.mask.from_surface(img)
    mask_outline = mask.outline()
    mask_surf = pygame.Surface(img.get_size())
    for pixel in mask_outline:
        mask_surf.set_at(pixel, (255, 255, 255))
    mask_surf.set_colorkey((0, 0, 0))
    screen.blit(mask_surf, (loc[0]-1, loc[1]))
    screen.blit(mask_surf, (loc[0]+1, loc[1]))
    screen.blit(mask_surf, (loc[0], loc[1]-1))
    screen.blit(mask_surf, (loc[0], loc[1]+1))

    
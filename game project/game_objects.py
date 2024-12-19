import pygame
import random
from assets import load_assets

class Star:
    def __init__(self, assets, screen_width, screen_height):
        self.image = assets["star"]
        self.rect = pygame.Rect(
            random.randint(screen_width, screen_width + 300),
            random.randint(20, screen_height - 20),
            self.image.get_width(),
            self.image.get_height(),
        )

    def move(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Projectile:
    def __init__(self, assets, screen_width, screen_height, hitbox_size=0.5):
        self.image = assets["asteroid"] 
        
      
        original_width, original_height = self.image.get_width(), self.image.get_height()
        
      
        scaled_width = int(original_width * hitbox_size)
        scaled_height = int(original_height * hitbox_size)
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))

       
        self.rect = pygame.Rect(
            random.randint(screen_width, screen_width + 300),
            random.randint(50, screen_height - 50),
            scaled_width,  # Use the scaled width
            scaled_height,  # Use the scaled height
        )

    def move(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

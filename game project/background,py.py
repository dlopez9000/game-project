import pygame

def draw_parallax_bg(screen):
    # Load and draw the background
    background_img = pygame.image.load('spacebg.png').convert()
    stars1 = pygame.image.load("stars1.png").convert_alpha()
    stars2 = pygame.image.load("stars2.png").convert_alpha()

    screen.blit(background_img, (0, 0))
    # Add parallax logic here if needed


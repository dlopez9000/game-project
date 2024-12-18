import pygame
from assets import load_assets


def draw_parallax_bg(screen, assets, scroll_stars1, scroll_stars2):
    stars1 = assets["stars1"]  # Access the stars1 asset correctly
    stars2 = assets["stars2"]

    stars1_width = stars1.get_width()
    stars2_width = stars2.get_width()

    # Main static background
    screen.blit(assets["background"], (0, 0))

    # Stars1 (slower parallax layer)
    for x in range(-1, screen.get_width() // stars1_width + 2):
        screen.blit(stars1, ((x * stars1_width) - (scroll_stars1 % stars1_width), 0))

    # Stars2 (faster parallax layer)
    for x in range(-1, screen.get_width() // stars2_width + 2):
        screen.blit(stars2, ((x * stars2_width) - (scroll_stars2 % stars2_width), 0))

import pygame
from assets import load_assets


def create_player(assets, screen_width, screen_height):
    nova_sprite = assets["nova_sprite"]
    player_rect = nova_sprite.get_rect(center=(screen_width // 2, screen_height // 2))
    return player_rect

def move_player(keys, player_rect, speed, screen_width, screen_height):
    if keys[pygame.K_w] and player_rect.top > 0:
        player_rect.y -= speed
    if keys[pygame.K_s] and player_rect.bottom < screen_height:
        player_rect.y += speed
    if keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= speed
    if keys[pygame.K_d] and player_rect.right < screen_width:
        player_rect.x += speed

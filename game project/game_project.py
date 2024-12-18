import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from assets import load_assets
from player import create_player, move_player
from background import draw_parallax_bg
import menu
import random
from pause import show_pause_menu 
import score_track
from game_over import display_game_over

# Constants
PLAYER_SPEED = 5
STARS1_SPEED = 2
STARS2_SPEED = 1
PROJECTILE_SPEED = 3  # Speed of falling projectiles
STAR_SPEED = 2  # Speed of falling stars

pygame.init()
pygame.mixer.init()

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nova The Space Dog")

# Load assets after display initialization
assets = load_assets()

# Function to restart the game
def restart_game():
    global player_rect, projectiles, stars, score, is_paused, running
    # Reset game variables
    projectiles = []
    stars = []
    score = 0
    is_paused = False
    player_rect = create_player(assets, SCREEN_WIDTH, SCREEN_HEIGHT)  # Reset player position
    running = True
    start_game_loop()  # Restart the game loop

# Main game loop
def start_game_loop():
    global running, projectiles, stars, score, is_paused

    # Create player
    player_rect = create_player(assets, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Projectile and star lists
    projectiles = []
    stars = []

    # Score counter
    score = 0
    font = pygame.font.SysFont('Comic Sans', 30)

    # Clock and timing
    clock = pygame.time.Clock()
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)  # Spawn a projectile every 1 second

    STAR_SPAWN_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(STAR_SPAWN_EVENT, 1500)  # Spawn a star every 1.5 seconds

    # Scroll variables for background
    scroll_stars1 = 0
    scroll_stars2 = 0

    # Play background music (spacetheme.mp3)
    pygame.mixer.music.load('spacetheme.mp3')
    pygame.mixer.music.play(-1, 0.0)  # Loop indefinitely

    # Show the menu screen before starting the game
    if menu.show_menu(screen, assets):
        running = True
        is_paused = False  # Track if the game is paused

        while running:
            keys = pygame.key.get_pressed()

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == SPAWN_EVENT:
                    # Spawn a new asteroid projectile at a random x position
                    x_pos = random.randint(0, SCREEN_WIDTH - assets["asteroid"].get_width())
                    y_pos = -assets["asteroid"].get_height()  
                    projectiles.append(pygame.Rect(x_pos, y_pos, assets["asteroid"].get_width(), assets["asteroid"].get_height()))
                elif event.type == STAR_SPAWN_EVENT:
                    # Spawn a new star at a random x position
                    x_pos = random.randint(0, SCREEN_WIDTH - assets["star"].get_width())
                    y_pos = -assets["star"].get_height()  # Start above the screen
                    stars.append(pygame.Rect(x_pos, y_pos, assets["star"].get_width(), assets["star"].get_height()))

                # Check for pause key (e.g., 'p')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # If 'p' is pressed, toggle pause
                        is_paused = not is_paused

            if is_paused:
                # Show the pause menu
                resume_game = show_pause_menu(screen, font)  # Assuming it returns a boolean for resuming
                if resume_game:
                    is_paused = False  # Unpause the game
                else:
                    running = False  # Quit the game if "Quit" is selected in the pause menu
                continue  # Skip the rest of the game loop when paused

            # Move player
            move_player(keys, player_rect, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Apply scaled hitbox for collision detection (0.5 scaling)
            scaled_player_rect = pygame.Rect(player_rect.centerx - player_rect.width * 0.25, 
                                             player_rect.centery - player_rect.height * 0.25, 
                                             player_rect.width * 0.5, 
                                             player_rect.height * 0.5)

            # Move projectiles
            for proj in projectiles:
                proj.y += PROJECTILE_SPEED  # Move down the screen

            # Move stars
            for star in stars:
                star.y += STAR_SPEED  # Move down the screen

            # Collision detection for stars (scaled hitbox)
            for star in stars[:]:
                if scaled_player_rect.colliderect(star):
                    stars.remove(star)  # Remove the star if collected
                    score += 1  # Increase score

            # Collision detection for projectiles (game over condition)
            for proj in projectiles:
                if scaled_player_rect.colliderect(proj):  # Game over if player collides with an asteroid
                    running = False  # End the game

            # Remove projectiles and stars that go off-screen
            projectiles = [proj for proj in projectiles if proj.y < SCREEN_HEIGHT]
            stars = [star for star in stars if star.y < SCREEN_HEIGHT]

            # Scroll background
            scroll_stars1 += STARS1_SPEED
            scroll_stars2 += STARS2_SPEED

            # Draw everything
            draw_parallax_bg(screen, assets, scroll_stars1, scroll_stars2)

            # Draw stars
            for star in stars:
                screen.blit(assets["star"], star)

            # Draw projectiles
            for proj in projectiles:
                screen.blit(assets["asteroid"], proj)

            # Draw player
            screen.blit(assets["nova_sprite"], player_rect)

 
           # Draw the score image
            score_image = assets["scoretally"]
            score_rect = score_image.get_rect(topleft=(10, 10))

# Draw the score image on the screen
            screen.blit(score_image, score_rect)

# Render the score text and position it next to the score image
            score_text = font.render(f"{score}", True, (255, 255, 255))  # White color for text

# The score text will be positioned to the right of the score image
            score_text_rect = score_text.get_rect(midleft=(score_rect.right + 10, score_rect.centery))  # Adjust position to the right of the image

# Draw the score text next to the score image
            screen.blit(score_text, score_text_rect)



            pygame.display.flip()
            clock.tick(60)

    # When the game ends, stop the music and display "Game Over"
    pygame.mixer.music.stop()

    # Call the game_over function to display the game over image and restart button
    display_game_over(screen, assets, restart_game)

# Start the game loop
start_game_loop()

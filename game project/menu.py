import pygame
import sys
import score_track  # Import the score tracking module
import settings

def show_menu(screen, assets):
    # Setup the menu screen
    font = pygame.font.SysFont('Arial', 40)
    title_image = assets['title_image']
    spacebar_image = assets['spacebar']
    scoresave_image = assets['scoresaved']  # Load the scoresave image
    logo_image = assets['logo']  # Load the logo image

    # Get the screen width and height for centering
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Load the last saved score
    last_score = score_track.load_score()

    # Game loop for the menu screen
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  # Fill screen with black color

        # Draw the title image (centered)
        title_rect = title_image.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(title_image, title_rect)

        # Draw the logo image (centered, above the spacebar and scoresaved images)
        logo_rect = logo_image.get_rect(center=(screen_width // 2, screen_height // 5))
        screen.blit(logo_image, logo_rect)

        # Adjust the positioning of the spacebar and scoresave images
        # Draw the spacebar sprite (centered, lower in the screen)
        spacebar_rect = spacebar_image.get_rect(center=(screen_width // 2, screen_height // 1.8))  # Move lower
        screen.blit(spacebar_image, spacebar_rect)

        # Draw the scoresave image (centered, lower in the screen)
        scoresave_rect = scoresave_image.get_rect(center=(screen_width // 2, screen_height // 1.3))  # Move lower
        screen.blit(scoresave_image, scoresave_rect)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if scoresave_rect.collidepoint(event.pos):
                    # Open a new window to show the saved score when clicking on scoresave image
                    show_score_window(last_score)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Spacebar pressed, start the game
                    menu_running = False  # Exit the menu loop and start the game

    return True  # Indicate that the game should start

def show_score_window(score):
    """Show a new window displaying the saved score."""
    # Create a new surface for the score window
    score_window = pygame.display.set_mode((400, 300), pygame.RESIZABLE)
    pygame.display.set_caption("Saved Score")

    font = pygame.font.SysFont('Arial', 60)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    # Game loop for the score window
    score_window_running = True
    while score_window_running:
        score_window.fill((0, 0, 0))  # Fill screen with black color

        # Draw the score text
        score_rect = score_text.get_rect(center=(200, 150))
        score_window.blit(score_text, score_rect)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score_window_running = False  # Exit score window loop
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):  # Close window on Escape or Enter
                    score_window_running = False

    # Restore the main game screen
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.quit()  # Quit the pygame window

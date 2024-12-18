import pygame

def display_game_over(screen, assets, restart_game_callback):
    """Display the game over image and restart button."""
    game_over_image = assets["gameover"]  # Load the game over image from assets
    restart_button_image = assets["restartbutton"]  # Load the restart button image
    game_over_screen = assets["gameoverscreen"]  # Load the game over screen background image

    # Get the screen dimensions to resize the background image
    screen_width, screen_height = screen.get_size()

    # Resize the game over screen to fit the entire screen
    game_over_screen = pygame.transform.scale(game_over_screen, (screen_width, screen_height))

    # Get the rect for the game over image to center it on the screen
    game_over_rect = game_over_image.get_rect(center=(screen_width // 2, screen_height // 2))
    restart_button_rect = restart_button_image.get_rect(center=(screen_width // 2, screen_height // 2 + 100))

    # Display the game over screen (background)
    screen.blit(game_over_screen, (0, 0))  # Draw the resized background image

    # Display the game over image and restart button
    screen.blit(game_over_image, game_over_rect)
    screen.blit(restart_button_image, restart_button_rect)

    pygame.display.flip()

    # Wait for a click on the restart button
    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(mouse_x, mouse_y):
                    restart_game_callback()  # Call the restart game function
                    waiting_for_restart = False
                    break

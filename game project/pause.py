import pygame

def show_pause_menu(screen, font):
    # Define pause menu options
    resume_text = font.render("Resume", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 0, 0))

    # Get screen dimensions to center the text
    screen_width, screen_height = screen.get_size()
    resume_rect = resume_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
    quit_rect = quit_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))

    # Load the pause image (ensure it's in the correct folder)
    pause_image = pygame.image.load("pauseimage.png")

    # Scale the pause image to match the screen size (optional)
    pause_image = pygame.transform.scale(pause_image, (screen_width, screen_height))

    # Display pause menu with the pause image as background
    screen.blit(pause_image, (0, 0))  # Draw the image to fill the screen
    screen.blit(resume_text, resume_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()

    # Wait for user input to resume or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_rect.collidepoint(event.pos):
                    return True  # Resume the game
                elif quit_rect.collidepoint(event.pos):
                    return False  # Quit the game

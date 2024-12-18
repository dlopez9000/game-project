import pygame
import os

# Function to save the score to a file
def save_score(score):
    try:
        with open("score.txt", "w") as file:
            file.write(str(score))
    except Exception as e:
        print(f"Error saving score: {e}")

# Function to load the score from a file
def load_score():
    try:
        if os.path.exists("score.txt"):
            with open("score.txt", "r") as file:
                return int(file.read())
        return 0  # Return 0 if no score file exists
    except Exception as e:
        print(f"Error loading score: {e}")
        return 0

# Function to display the score window
def display_score_window(screen, assets, font):
    # Load score from the file
    score = load_score()

    # Create a new window (the same size as the game window)
    screen.fill((0, 0, 0))  # Black background

    # Draw the score saved message
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 3))

    # Draw a back button to return to the menu
    back_button = assets["restartbutton"]
    back_button_rect = back_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    screen.blit(back_button, back_button_rect)

    pygame.display.flip()

    # Handle events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return True  # Go back to the menu
    return True

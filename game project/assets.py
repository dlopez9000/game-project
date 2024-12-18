import pygame

def load_assets():
    assets = {}

    try:
     assets["background"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\spacebg.png").convert()
     assets["nova_sprite"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\novasprite.png").convert_alpha()
     assets["stars2"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\stars2.png").convert_alpha()
     assets["star"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\star.png").convert_alpha()
     assets["asteroid"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\asteroid.png").convert_alpha()
     assets["title_image"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\titleimage.png").convert()
     assets["spacebar"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\spacebar.png").convert_alpha()
     assets["stars1"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\stars1.png").convert_alpha()
     assets["pause_image"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\pauseimage.png").convert_alpha()
     assets["scoresaved"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\scoresaved.png").convert_alpha()
     assets["gameover"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\gameover.png").convert_alpha()
     assets["restartbutton"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\restartbutton.png").convert_alpha()
     assets["scoretally"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\scoretally.png").convert_alpha()
     assets["gameoverscreen"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\gameoverscreen.png").convert_alpha()
     assets["logo"] = pygame.image.load("C:\\Users\\unico\\source\\repos\\game project\\game project\\logo.png").convert_alpha()
    except pygame.error as e:
        print(f"Error loading images: {e}")
        raise SystemExit("Failed to load images.")

    # Load sounds
    try:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Error loading sound: {e}")
        raise SystemExit("Failed to load sound.")

    return assets



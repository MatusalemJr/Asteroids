import pygame
from constants import *
from player import Player

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    running = True
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_colour = (0, 0, 0)

    player = Player(
        x=SCREEN_WIDTH / 2,  
        y=SCREEN_HEIGHT / 2
    )
    
    while running:
        # Fill screen with black
        screen.fill(screen_colour)
        
        # Draw the player
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

  

if __name__ == "__main__":
    main()


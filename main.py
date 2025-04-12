import pygame
from constants import *
print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    running = True
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_colour = (0, 0, 0)
    while running:
        screen.fill(screen_colour)
        pygame.display.flip()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

if __name__ == "__main__":
    main()


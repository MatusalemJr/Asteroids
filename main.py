import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

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
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    player = Player(
        x=SCREEN_WIDTH / 2,  
        y=SCREEN_HEIGHT / 2
    )

    while running:
        # Calculate dt at the beginning of each frame
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()

        # Fill screen with black
        screen.fill(screen_colour)
        
        # Draw the player
        for entity in drawable:
            entity.draw(screen)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()


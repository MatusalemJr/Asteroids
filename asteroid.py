from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if hasattr(Asteroid, 'containers'):
            for group in Asteroid.containers:
                group.add(self)
        
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2.velocity = new_velocity2 * 1.2

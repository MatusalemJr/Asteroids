import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        current_class = self.__class__
        if hasattr(current_class, "containers"):
            pygame.sprite.Sprite.__init__(self, current_class.containers)
        else:
            pygame.sprite.Sprite.__init__(self)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        return distance <= (self.radius + other_shape.radius)
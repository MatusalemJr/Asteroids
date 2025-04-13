from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shot_cooldown = 0

        if hasattr(Player, 'containers'):
            for group in Player.containers:
                group.add(self)
                
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shoot()
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
       # Create a new shot at the player's position
       shot_x = self.position.x
       shot_y = self.position.y
    
       # Calculate velocity: start with vector (0, 1), rotate it, then scale it
       velocity = pygame.Vector2(0, 1)
       velocity = velocity.rotate(self.rotation)
       velocity *= PLAYER_SHOOT_SPEED
    
       # Create the shot with the calculated velocity
       Shot(shot_x, shot_y, velocity)

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
        if hasattr(Shot, 'containers'):
            for group in Shot.containers:
                group.add(self)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
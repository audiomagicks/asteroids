import pygame # type: ignore
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        newv1 = self.velocity.rotate(angle)
        newv2 = self.velocity.rotate(-angle)
        newrad = self.radius - ASTEROID_MIN_RADIUS
        newroid1 = Asteroid(self.position.x, self.position.y, newrad)
        newroid2 = Asteroid(self.position.x, self.position.y, newrad)
        newroid1.velocity = newv1
        newroid2.velocity = newv2
        newroid1.velocity *= 1.2
        newroid2.velocity *= 1.2

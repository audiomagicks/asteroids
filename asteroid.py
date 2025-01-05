import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = super.velocity
        
        
    
    def draw(self, screen, position, radius):
        pygame.draw.circle(screen, "gray", position, radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
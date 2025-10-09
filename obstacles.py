# obstacles.py
"""
Defines the Obstacle base class and its various child classes.
"""
import pygame
import random
import config

class Obstacle(pygame.sprite.Sprite):
    """Base class for all obstacles."""
    def __init__(self, x, y, width, height, color, obstacle_type="obstacle"):
        super().__init__()
        self.obstacle_type = obstacle_type
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        """Move the obstacle down the screen."""
        self.rect.y += config.OBSTACLE_SPEED
        if self.is_off_screen():
            self.kill() # Remove the sprite if it's off-screen

    def get_score_impact(self):
        """Returns the score impact of this obstacle (e.g., -10 for collision)."""
        return -10

    def is_off_screen(self):
        """Checks if the obstacle is below the screen."""
        return self.rect.top > config.SCREEN_HEIGHT

    def get_bounds(self):
        """Returns the rectangle defining the obstacle's bounds."""
        return self.rect

# --- Specific Obstacle Types ---

class Car(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 80, config.YELLOW, "Car")

class Truck(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 120, config.GREEN, "Truck")

class Bus(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 70, 150, config.CYAN, "Bus")
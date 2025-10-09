# player.py
"""
Defines the PlayerCar class, controlled by the user.
"""
import pygame
from vehicle import VehicleMovement
import config

class PlayerCar(VehicleMovement):
    """
    Represents the player's car. Inherits from VehicleMovement.
    """
    def __init__(self, x, y):
        super().__init__(x, y, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, config.PLAYER_MAX_SPEED, config.BLUE)
        self.score = 0
        self.max_speed = config.PLAYER_MAX_SPEED
        self.is_alive = True

    def accelerate(self):
        # Placeholder for acceleration logic
        print("Accelerating...")

    def move_left(self):
        """Moves the car to the left."""
        self.move(-self.speed, 0)

    def move_right(self):
        """Moves the car to the right."""
        self.move(self.speed, 0)
        
    def is_within_bounds(self):
        """Keeps the player within the screen bounds."""
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH

    def check_collision(self, obstacle_group):
        """Checks for collision with any obstacle in the given group."""
        if pygame.sprite.spritecollide(self, obstacle_group, False):
            self.is_alive = False

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def set_alive(self, status):
        self.is_alive = status

    def update(self):
        """Update method called every frame."""
        self.is_within_bounds()
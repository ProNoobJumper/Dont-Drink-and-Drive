# vehicle.py
"""
Defines the base class for any moving vehicle in the game.
"""
import pygame

class VehicleMovement(pygame.sprite.Sprite):
    """
    A base class for movable vehicle objects.
    Inherits from pygame.sprite.Sprite for built-in game functionalities.
    """
    def __init__(self, x, y, width, height, speed, color=WHITE):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.speed = speed

        # Pygame sprite attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_pos, self.y_pos)

    def move(self, dx, dy):
        """Moves the vehicle by a given delta x and delta y."""
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        """Draws the vehicle on the provided screen."""
        screen.blit(self.image, self.rect)

    def getPosition(self):
        """Returns the current (x, y) position."""
        return (self.rect.x, self.rect.y)

    def setPosition(self, x, y):
        """Sets the vehicle's position to a new (x, y)."""
        self.rect.x = x
        self.rect.y = y
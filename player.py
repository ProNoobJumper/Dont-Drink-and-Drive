import pygame
from vehicle import VehicleMovement
import config

class PlayerCar(VehicleMovement):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, config.PLAYER_MAX_SPEED, config.BLUE, config.PLAYER_IMAGE, *groups)
        self.score = 0
        self.max_speed = config.PLAYER_MAX_SPEED
        self.is_alive = True
        self.acceleration = 0.5
        self.current_speed = 0.0
        
        # Create a separate hitbox rectangle
        self.hitbox = pygame.Rect(0, 0, config.PLAYER_HITBOX_WIDTH, config.PLAYER_HITBOX_HEIGHT)
        self.hitbox.center = self.rect.center

    def accelerate(self):
        self.move(0, -self.speed)

    def decelerate(self):
        self.move(0, self.speed)

    def move_left(self):
        self.move(-self.speed, 0)

    def move_right(self):
        self.move(self.speed, 0)
        
    def move(self, dx, dy):
        # Override the parent's move method to update the hitbox
        super().move(dx, dy)  # This moves self.rect
        self.hitbox.center = self.rect.center # Re-center the hitbox

    def is_within_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > config.SCREEN_HEIGHT:
            self.rect.bottom = config.SCREEN_HEIGHT
        
        # Update hitbox position after clamping rect
        self.hitbox.center = self.rect.center

    def check_collision(self, obstacle_group):
        # New simplified collision logic
        # It checks for collision between the player's hitbox
        # and each obstacle's hitbox.
        for obstacle in obstacle_group:
            if self.hitbox.colliderect(obstacle.hitbox):
                self.is_alive = False
                return

    def update(self):
        pass
        self.is_within_bounds()
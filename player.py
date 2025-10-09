import pygame
from vehicle import VehicleMovement
import config

class PlayerCar(VehicleMovement):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, config.PLAYER_MAX_SPEED, config.BLUE, config.PLAYER_IMAGE, *groups)
        self.score = 0
        self.max_speed = config.PLAYER_MAX_SPEED
        self.is_alive = True
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    def accelerate(self):
        # Placeholder for acceleration logic
        print("Accelerating...")
=======
=======
>>>>>>> Stashed changes
        self.acceleration = 0.5
        self.current_speed = 0.0

    def accelerate(self):
        self.current_speed = min(self.current_speed + self.acceleration, self.max_speed)

    def decelerate(self):
        self.current_speed = max(self.current_speed - self.acceleration, -self.max_speed / 2)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    def move_left(self):
        self.move(-self.speed, 0)

    def move_right(self):
        self.move(self.speed, 0)
        
    def is_within_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > config.SCREEN_HEIGHT:
            self.rect.bottom = config.SCREEN_HEIGHT

    def check_collision(self, obstacle_group):
        # Use a reduced hitbox for the player for more forgiving collisions
        ratio = max(0.0, min(1.0, config.HITBOX_RATIO))
        reduced_w = int(self.rect.width * ratio)
        reduced_h = int(self.rect.height * ratio)
        reduced_rect = pygame.Rect(0, 0, reduced_w, reduced_h)
        # Center the reduced rect on the player's rect
        reduced_rect.center = self.rect.center

        for obstacle in obstacle_group:
            # Optionally reduce obstacle hitbox as well if desired
            obs_w = int(obstacle.rect.width * ratio)
            obs_h = int(obstacle.rect.height * ratio)
            obs_rect = pygame.Rect(0, 0, obs_w, obs_h)
            obs_rect.center = obstacle.rect.center
            if reduced_rect.colliderect(obs_rect):
                self.is_alive = False
                return
<<<<<<< Updated upstream

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def set_alive(self, status):
        self.is_alive = status

    def update(self):
<<<<<<< Updated upstream
        """Update method called every frame."""
=======
        vertical_dy = -int(self.current_speed)
        self.move(0, vertical_dy)
>>>>>>> Stashed changes
=======

    def update(self):
        vertical_dy = -int(self.current_speed)
        self.move(0, vertical_dy)
>>>>>>> Stashed changes
        self.is_within_bounds()
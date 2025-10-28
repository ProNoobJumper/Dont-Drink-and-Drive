import pygame
import random
import config

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, hitbox_width, hitbox_height, color, obstacle_type="obstacle"):
        super().__init__()
        self.obstacle_type = obstacle_type
        self.passed = False
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Create the hitbox
        self.hitbox = pygame.Rect(0, 0, hitbox_width, hitbox_height)
        self.hitbox.center = self.rect.center

    def update(self):
        self.rect.y += config.CURRENT_OBSTACLE_SPEED
        self.hitbox.center = self.rect.center  # Keep hitbox centered on rect
        if self.is_off_screen():
            self.kill()

    def get_score_impact(self):
        return -10

    def is_off_screen(self):
        return self.rect.top > config.SCREEN_HEIGHT

    def get_bounds(self):
        return self.rect


class Car(Obstacle):
    def __init__(self, x, y):
        # Pass hitbox dimensions to the base class
        super().__init__(x, y, 
                         config.CAR_WIDTH, config.CAR_HEIGHT, 
                         config.CAR_HITBOX_WIDTH, config.CAR_HITBOX_HEIGHT, 
                         config.YELLOW, "Car")
        if config.CAR_IMAGE:
            try:
                img = pygame.image.load(config.CAR_IMAGE).convert_alpha()
                self.image = pygame.transform.scale(img, (config.CAR_WIDTH, config.CAR_HEIGHT))
                self.rect = self.image.get_rect(topleft=(x, y))
                self.hitbox.center = self.rect.center  # Re-center hitbox
            except Exception:
                pass

class Truck(Obstacle):
    def __init__(self, x, y):
        # Pass hitbox dimensions to the base class
        super().__init__(x, y, 
                         config.TRUCK_WIDTH, config.TRUCK_HEIGHT, 
                         config.TRUCK_HITBOX_WIDTH, config.TRUCK_HITBOX_HEIGHT, 
                         config.GREEN, "Truck")
        if config.TRUCK_IMAGE:
            try:
                img = pygame.image.load(config.TRUCK_IMAGE).convert_alpha()
                self.image = pygame.transform.scale(img, (config.TRUCK_WIDTH, config.TRUCK_HEIGHT))
                self.rect = self.image.get_rect(topleft=(x, y))
                self.hitbox.center = self.rect.center  # Re-center hitbox
            except Exception:
                pass

class Bus(Obstacle):
    def __init__(self, x, y):
        # Pass hitbox dimensions to the base class
        super().__init__(x, y, 
                         config.BUS_WIDTH, config.BUS_HEIGHT, 
                         config.BUS_HITBOX_WIDTH, config.BUS_HITBOX_HEIGHT, 
                         config.CYAN, "Bus")
        if config.BUS_IMAGE:
            try:
                img = pygame.image.load(config.BUS_IMAGE).convert_alpha()
                self.image = pygame.transform.scale(img, (config.BUS_WIDTH, config.BUS_HEIGHT))
                self.rect = self.image.get_rect(topleft=(x, y))
                self.hitbox.center = self.rect.center  # Re-center hitbox
            except Exception:
                pass
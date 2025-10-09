import pygame
import config

class VehicleMovement(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, color=config.WHITE, image_path=None, *groups):
        super().__init__(*groups)
        self.x_pos = x
        self.y_pos = y
        self.speed = speed

        if image_path:
            try:
                loaded = pygame.image.load(image_path).convert_alpha()
                self.image = pygame.transform.scale(loaded, (width, height))
            except Exception:
                self.image = pygame.Surface([width, height])
                self.image.fill(color)
        else:
            self.image = pygame.Surface([width, height])
            self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_pos, self.y_pos)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getPosition(self):
        return (self.rect.x, self.rect.y)

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
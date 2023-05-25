import random
import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
    def __init__(self, image, type):
        self.image = image
        self.image = pygame.transform.scale(self.image, (22*2, 20*2))
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800,1000)
        self.rect.y = random.randint(125,320)

        self.start_time = 0
        self.duration = random.randint(5,10)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
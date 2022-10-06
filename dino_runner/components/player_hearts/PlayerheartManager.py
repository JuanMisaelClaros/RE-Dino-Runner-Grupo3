import pygame
from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import HEART_COUNT

class PlayerheartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT

    def reduce_heart(self):
        self.heart_count = self.heart_count -1

    def draw(self, screen):
        x_position = 10
        y_position = 20

        for counter in range(self.heart_count):
            heart = Heart(x_position,y_position)  
            heart.draw(screen) 
            x_position = x_position + 30

    def resert_heart(self):
        self.heart_count = HEART_COUNT        

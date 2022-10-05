from itertools import count
import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS=80
    Y_POS=310
    Y_POS_DUCK=340
    JUMP_LEVEL=8.5
    count = 0

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.jump_vel = self.JUMP_LEVEL

        self.step_index=0

    def update(self,user_input):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()

        if user_input[pygame.K_DOWN] and not self.dino_jump :
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        if user_input[pygame.K_UP] and not self.dino_jump :
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True    

        if not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index == 10:
            self.step_index = 0


    def run(self):
        self.step_index = self.step_index + 1
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        print(self.step_index)
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index = self.step_index + 1

    def jump(self):
        self.image = JUMPING
        if(self.dino_jump):
            self.dino_rect.y = self.dino_rect.y - (self.jump_vel *4)
            self.jump_vel = self.jump_vel - 1

        if(self.jump_vel < -self.JUMP_LEVEL):
               self.dino_rect.y =  self.Y_POS
               self.dino_jump = False
               self.jump_vel = self.JUMP_LEVEL
               
    
    def draw(self,screen):
        screen.blit(self.image, ( self.dino_rect.x, self.dino_rect.y) )       

import pygame
from laser import Laser


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("Gfx/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height))
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()


    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE]:
            laser = Laser(self.rect.center, 5, self.screen_height)
            self.lasers_group.add(laser)


    def update(self):
        self.get_user_input()
        self.constrain_movement()#2 aggiunta in loop del blocco della naveta sullo schermo
        self.lasers_group.update()

    def constrain_movement(self):#1 blocco della navetta all interno dello schermo
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

        





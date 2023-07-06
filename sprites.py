import pygame.sprite

import maps.map1, maps.map2
from maps.map1 import map_data
from properties import *


""" parentclass for tile-creation with params that are in common with its children (e.g. Platform-class) """
class Sprites(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (tile_size_x, tile_size_y)) # scale tiles by windows-dimensions
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

""" moving-platforms """
class Platform(Sprites):
    def __init__(self, x, y, img, movex, movey, steps):
        super().__init__(x, y, img)
        self.steps = steps
        self.move_counter = 0
        self.move_dir = 1
        self.moveX = movex  # steps to move in x dir
        self.moveY = movey  # steps to move in y dir

    def update(self):
        # platform movement
        self.rect.x += self.move_dir * self.moveX
        self.rect.y += self.move_dir * self.moveY
        self.move_counter += 1
        # counting to an absolut of fifty steps for movement and either subtracting or adding until 50/-50 is reached
        if abs(self.move_counter) >= self.steps:
            self.move_dir *= -1
            self.move_counter *= -1


class Enemy(Sprites):
    def __init__(self, x, y, steps, img, g):
        super().__init__(x, y, img)
        self.g = g
        self.steps = steps
        self.img_right = pygame.transform.scale(img, (tile_size_x*1, tile_size_y*1))
        self.img_left = pygame.transform.flip(self.img_right, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_dir = 1
        self.hitbox = self.image.get_rect() # add a seperate hitbox for better game feeling

    """ extendes pygame-update-function
    flip image when direction changes, move enemy according to direction, and enemy-movement similiar to platform-movement"""
    def update(self):
        if self.move_dir == -1:
            self.image = self.img_left
        else:
            self.image = self.img_right

        self.rect.x += self.move_dir * 1
        self.move_counter += 1
        # counting to an absolut number of steps for movement and either subtracting or adding until 50/-50 is reached
        if abs(self.move_counter) >= self.steps :
            self.move_dir *= -1
            self.move_counter *= -1


class Missile(Sprites):
    def __init__(self, x, y, img, playerdirection):
        super().__init__(x, y, img)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (20, 20))
        if playerdirection == 0:
            self.direction = 1
        else:
            self.direction = playerdirection
        self.moveX = 15


    """ standard pygame-update-function extended to move and if moves out of screen, delete itself"""
    def update(self):
        self.rect.x += self.moveX * self.direction 
        if self.rect.x >= screen_width or self.rect.x <= 0: 
            self.kill()

""" Exit/Clear world and load next world """
class ExitGate(Sprites):
    def __init__(self, x, y, img):
        super().__init__(x, y, img) # looks better, when a bit wider
        self.image = pygame.transform.scale(img, (tile_size_x/1.5, tile_size_y))


class Coin(Sprites):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)


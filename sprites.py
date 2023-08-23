import pygame.sprite
from properties import *


""" Parentclass used for simple sprites like dirt and grassblocks - children inherit basic properties """
class Sprites(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (tile_size_x, tile_size_y)) # scale tilesize by window-dimensions (properties.py)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

""" moving-platforms
    functions like enemies, increasing the x/y position until reaching an absolute number of steps and then inverting the movement-direction 
     platforms move the player in there x/y-direction, see playerclass - collision method
"""
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
        # The platform is constantly moving while counting it's steps. When the absolute count is equivalent to the "steps"-constant, the direction is inverted
        # the absolute number will always be positive, the direction is inverted when reaching +50 and subtracts until -50 is reached and using addition again
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
        self.hitbox = self.image.get_rect() # adds a seperate hitbox to adjust the collision
        self.hitbox.height = self.rect.height * 0.75 # a smaller hitbox feels less frustrating
        self.hitbox.width = self.rect.width * 0.5


    def update(self):
        if self.move_dir == -1:         #flip the image when direction changes
            self.image = self.img_left
        else:
            self.image = self.img_right

        self.rect.x += self.move_dir * 1
        self.move_counter += 1
        # counting to an absolut number of steps for movement and either subtracting or adding until 50/-50 is reached
        if abs(self.move_counter) >= self.steps :
            self.move_dir *= -1
            self.move_counter *= -1
        self.hitbox.x = self.rect.x + (self.hitbox.width // 2 ) # hitbox must follow the rect and image of the enemy
        self.hitbox.y = self.rect.y  + (self.hitbox.height / 8)

class Missile(Sprites):
    def __init__(self, x, y, img, playerdirection):
        super().__init__(x, y, img)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (20, 20))
        if playerdirection == 0:
            self.direction = 1  # movement direction aligns with the player's direction
        else:
            self.direction = playerdirection
        self.moveX = 15 # movex is the amount of steps, the missile moves every tick


    #the missile is killed, as soon as it its position reaches the maximum screen-dimensions
    def update(self):
        self.rect.x += self.moveX * self.direction 
        if self.rect.x >= screen_width or self.rect.x <= 0: # out of screen
            self.kill()

""" ExitGate to enter and load next world """
class ExitGate(Sprites):
    def __init__(self, x, y, img):
        super().__init__(x, y, img) # looks better, when a bit wider
        self.image = pygame.transform.scale(img, (tile_size_x/1.5, tile_size_y))

# This child-class is redundant and does not differ from Sprite-Class, besides it's name
class Coin(Sprites):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)


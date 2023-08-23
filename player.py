import pygame
from sprites import Missile
from properties import *


""" Playerclass contains the handling of the Playersprite and collision/interaction with other sprites, Playermotion, movement etc.
    gameAttr is referencing a variable through which we can access the whole instace of Gameclass and it's instance variables
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, gameAttr):
        pygame.sprite.Sprite.__init__(self)
        self.jumped = False
        self.isdead = False
        self.in_air = True
        # references the instance of GameHandler to access all of its attributes
        self.gameAttr = gameAttr
        # direction for left/right walking animation
        self.direction = 0
        # position vector | velocity x/y vectors
        vector = pygame.math.Vector2
        self.vel = vector(0, 0)
        # x and y displacement, distance moved in one direction variable is used for reverting movement when colliding with objects
        self.dx = 0
        self.dy = 0
        self.pos = vector(x, y)
        # list to memorize gametime ticks
        self.ptick = [pygame.time.get_ticks()]
        # animation-vars
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.loadAnimationSprites()
        self.counter = 0
        self.walk_cooldown = 6
        # rectangle properties
        self.rect = self.images_right[1].get_rect()
        self.width = self.images_right[1].get_width()
        self.height = self.images_right[1].get_height()-10
        self.rect.x = x
        self.rect.y = y


    """ update function called by Gameclass-update"""
    def update(self):
        # reset velocity and directional movement
        self.dx = 0
        self.dy = 0
        self.vel.x = 0
        self.movement()
        self.gravity()
        self.animate()
        self.collision()
        # update player coordinates, after collision to reverse changes in position
        self.rect.x += self.dx
        self.rect.y += self.dy
        # draw player onto screen




    def collision(self):
        """ first loop through moving platforms, when playerpos + y-movement collides with platform:
         add directional platform-movement to the x-movement of the player
         y-movement of the player stays unchanged (the player is technically falling, the y-movement gets reset in the next loop)
         the collision is handles using colliderect sometimes with parameters besides colliding object, to specify the recttangle-borders colliding"""
        self.in_air = True
        for tile in self.gameAttr.tile_list:
            # check for collision in x direction, revert x-displacement when colliding
            if tile.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            # check for collision in y direction
            #pygame.rect.Rect.colliderect()
            #if tile.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
            if tile.rect.colliderect(self.rect.left, self.rect.top + self.dy, self.width, self.height):
                # check if below the ground for example, jumping while under a block
                if self.vel.y < 0:
                    self.dy = tile.rect.bottom - self.rect.top
                    self.vel.y = 0
                # check if above the ground i.e. falling
                elif self.vel.y >= 0:
                    self.dy = tile.rect.top - self.rect.bottom
                    self.vel.y = 0
                    self.in_air = False
        for enemy in self.gameAttr.enemy_sprites: # the players dies when an enemy collides with him
            if self.rect.colliderect(enemy.hitbox):
                self.isdead = True
                self.coins = 0
            #pygame.draw.rect(self.gameAttr.screen,0, enemy.hitbox)
            # kill the enemy and sprite, when collide
            # draw the hitbox of the enemy in comment above
            for missile in self.gameAttr.missile_sprites: # the enemy dies, should it collide with a missile(which is also killed)
                if missile.rect.colliderect(enemy):
                    missile.kill()
                    enemy.kill()
        for tile in self.gameAttr.ExitGroup:
            if tile.rect.colliderect(self):
                self.gameAttr.nextWorld()  # the world is reset and the next one loaded
        for coin in self.gameAttr.CoinGroup:
            self.coins = abs(self.gameAttr.coins)
            if self.rect.colliderect(coin.rect):
                self.gameAttr.coins += 1
                coin.kill()
        for plat in self.gameAttr.platform_group:
            if plat.rect.colliderect(self.rect.left, self.rect.top + self.dy + 5, self.width, self.height):
                self.dx += plat.move_dir

    """ function for keyinput handling and player movement + animation """
    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel.y = -14
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT] and key[pygame.K_RIGHT]:
            self.animate(False)
        elif key[pygame.K_LEFT]:
            self.dx -= 5
            self.counter += 1
            self.direction = -1
        elif key[pygame.K_RIGHT]:
            self.dx += 5
            self.counter += 1
            self.direction = 1
        else:
            self.animate(False)
        if key[pygame.K_TAB]: # new missile entity is spawned moving in the direction of the player
            self.ptick.append(pygame.time.get_ticks())
            for tick in self.ptick:
                if tick >= self.ptick[0] + 100: # every 100ticks, spawn a new missile
                    self.pew = Missile(self.rect.x, self.rect.y, missile_img, self.direction)
                    self.gameAttr.all_sprites.add(self.pew)
                    self.gameAttr.missile_sprites.add(self.pew)
                    self.ptick.clear()

    """gravity simply adds consistent y-movement, to make the player fall. Not pretty, but convenient"""
    def gravity(self):
        #   constantly add y velocity to speed up the fall
        if self.in_air == True:
            self.vel.y += 1.2
        # limit max falling-speed
        if self.vel.y > 18:
           self.vel.y = 18
        self.dy += self.vel.y

    # walkcycle animation looping through the sprites
    def animate(self, walking = None):
        if self.counter > self.walk_cooldown: # spacing out the animationcycle
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        if walking == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        self.height = self.image.get_height()


    """ loading sprites in loop, setup for player-rect and img
      for each iteration, animation-sprite and index are loaded, stored in self.images_l/r"""
    def loadAnimationSprites(self):
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, ((screen_height / screen_width)*40, (screen_height / screen_width)*50))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            self.image = self.images_right[self.index]


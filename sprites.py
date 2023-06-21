import pygame.sprite

from maps.map import map_data
from properties import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, gameAttr):
        pygame.sprite.Sprite.__init__(self)
        self.jumped = False
        self.dead = False
        self.in_air = True
        # Pass attributes of class Game
        self.gameAttr = gameAttr
        # direction for left/right walking animation
        self.direction = 0
        # position vector | velocity and acceleration as x/y vectors
        vector = pygame.math.Vector2
        self.vel = vector(0, 0)
        # x and y displacement, distance moved in one direction variable is used for reverting movement when colliding with objects
        self.dx = 0
        self.dy = 0
        # list to memorize gametime ticks
        self.ptick = [pygame.time.get_ticks()]
        # animation-vars
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.loadAnimationSprites()
        self.counter = 0
        self.walk_cooldown = 8
        # rectangle properties
        self.rect = self.images_right[1].get_rect()
        self.width = self.images_right[1].get_width()
        self.height = self.images_right[1].get_height()-10

        #self.width = player_img_right1.get_width()
        #self.height = player_img_right1.get_height()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.dx = 0
        self.dy = 0
        self.vel.x = 0
        self.walk_cooldown = 8
        self.movement()
        self.gravity()
        self.animate()
        self.collision()
        self.update_pos()

        # draw player onto screen
        self.gameAttr.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.gameAttr.screen, (255, 255, 255), self.rect, 1)

    def update_pos(self):
        # update player coordinates
        self.rect.x += self.dx
        self.rect.y += self.dy

    def collision(self):
        # update in_air to check if the player is walking/falling down independent of the player jumping
        self.in_air = True
        # first loop through moving platforms, when playerpos + y-movement collides with platform:
        # add directional platform-movement to the x-movement of the player
        # y-movement of the player stays unchanged (the player is technically falling, the y-movement gets reset in the next loop)
        for plat in self.gameAttr.platform_group:
            if plat.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.vel.y >= 0:
                    self.dx += plat.move_dir
        for tile in self.gameAttr.tile_list:
            # check for collision in x direction, revert x-displacement when colliding
            if tile.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            # check for collision in y direction
            if tile.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                # check if below the ground for example, jumping while under a block
                if self.vel.y < 0:
                    self.dy = tile.rect.bottom - self.rect.top
                    self.vel.y = 0
                # check if above the ground i.e. falling
                elif self.vel.y >= 0:
                    self.dy = tile.rect.top - self.rect.bottom
                    self.vel.y = 0
                    self.in_air = False
        # delete enemy and missile on collision
        for enemy in self.gameAttr.enemy_sprites:
            if enemy.rect.colliderect(self):
                self.gameAttr.dead = True
            for missile in self.gameAttr.missile_sprites:
                if missile.rect.colliderect(enemy):
                    missile.kill()
                    enemy.kill()

    # function for keyinput-initiated player movement + animationcall
    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel.y = -15
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
        if key[pygame.K_TAB]:
            self.ptick.append(pygame.time.get_ticks())
            for tick in self.ptick:
                if tick >= self.ptick[0] + 100:
                    pew = Missile(self.rect.x, self.rect.y, missile_img, self.direction)
                    self.gameAttr.missile_sprites.add(pew)
                    self.ptick.clear()

    def gravity(self):
        # gravity by adding consistent y-movement instead of potentiating the velocity by acceleration
        self.vel.y += 1
        if self.vel.y > 10:
            self.vel.y = 10
        self.dy += self.vel.y

    # walkcycle animation looping through the sprites
    def animate(self, walking = None):
        if self.counter > self.walk_cooldown:
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


    # loading sprites in loop, setup for player-rect and img
    # for each animation-sprite load iteration and index
    def loadAnimationSprites(self):
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, ((screen_height / screen_width)*40, (screen_height / screen_width)*50))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

    def isdead(self):
        return self.dead


# world class used for loading the tilemap and assigning and grouping sprites
# the for loops are reading every line and row of the tilemap-document and therefore giving each symbol a x and y coordinate
class World():
    def __init__(self, gameAttr):
        self.gameAttr = gameAttr
        self.all_sprites = pygame.sprite.Group()
        row_count = 0
        for row in map_data:
            col_count = 0
            for tile in row:
                x = col_count * tile_size_x
                y = row_count * tile_size_y
                if tile == 1:
                    self.tile = Sprites(x, y, dirt_img)
                    self.gameAttr.tile_list.append(self.tile)
                if tile == 2:
                    self.tile = Sprites(x, y, grass_img)
                    self.gameAttr.tile_list.append(self.tile)
                if tile == "x":
                    self.tile = Platform(x, y, platform_img, 1, 0)
                    self.gameAttr.tile_list.append(self.tile)
                    self.gameAttr.platform_group.add(self.tile)
                if tile == "y":
                    self.tile = Platform(x, y, platform_img, 0, 1)
                    self.gameAttr.tile_list.append(self.tile)
                    self.gameAttr.platform_group.add(self.tile)
                if tile == "E":
                    self.tile = Enemy(x, y - 10, enemy_img)
                    self.gameAttr.enemy_sprites.add(self.tile)
                self.all_sprites.add(self.tile)
                col_count += 1
            row_count += 1

    def update(self):
        for tile in self.all_sprites:
            pygame.draw.rect(self.gameAttr.screen, (255, 255, 255), tile.rect, -1)
        self.all_sprites.draw(self.gameAttr.screen)
        self.gameAttr.missile_sprites.update()
        self.gameAttr.missile_sprites.draw(self.gameAttr.screen)
        self.gameAttr.enemy_sprites.update()
        self.gameAttr.platform_group.update()


# simple parentclass for tile-creation with params that are in common with its children (e.g. Platform-class)
class Sprites(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (tile_size_x, tile_size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# moving platforms
class Platform(Sprites):
    def __init__(self, x, y, img, moveX, moveY):
        super().__init__(x, y, img)
        self.move_counter = 0
        self.move_dir = 1
        self.moveX = moveX  # steps to move in x dir
        self.moveY = moveY  # steps to move in y dir

    def update(self):
        self.rect.x += self.move_dir * self.moveX
        self.rect.y += self.move_dir * self.moveY
        self.move_counter += 1
        # counting to an absolut of fifty steps for movement and either subtracting or adding until 50/-50 is reached
        if abs(self.move_counter) >= 50:
            self.move_dir *= -1
            self.move_counter *= -1


class Enemy(Sprites):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
        self.image = pygame.transform.scale(img, (tile_size_y, tile_size_x))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_dir = 1

    def update(self):
        self.move_counter += 1
        if abs(self.move_counter) >= 120:
            self.move_dir *= -1
            self.move_counter *= -1
        self.rect.x += (self.move_counter * self.move_dir) / 80


class Missile(Sprites):
    def __init__(self, x, y, img, direction):
        super().__init__(x, y, img)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (20, 20))
        if direction == 0:
            self.direction = 1
        else:
            self.direction = direction
        self.moveX = 15

    def update(self):
        self.rect.x += self.moveX * self.direction
        #self.screen.blit(self.image, self.rect)
        if self.rect.x >= screen_width or self.rect.x <= 0:
            self.kill()

import pygame
from properties import *
from sprites import Sprites, Platform, Enemy, ExitGate, Coin


""" world class used for creating the world by loading the world-data-files and updating/drawing there sprites """
class World():
    def __init__(self, gameAttr, map):
        self.map = map
        self.gameAttr = gameAttr
        self.all_sprites = self.gameAttr.all_sprites

        self.fetchmap(self.map)


    """ every world_data file contains 20 rows and columns, where each element is a Number or letter corresponding to one sprite """
    def fetchmap(self, map):
        row_count = 0
        self.map = map
        for row in self.map:
            col_count = 0
            for tile in row: # sprites are placed in the world by multiplying the tile-wideness by column of the tile and tile-height multiplied by row
                x = col_count * tile_size_x
                y = row_count * tile_size_y
                if tile == 1:
                    self.tile = Sprites(x, y, dirt_img)
                    self.gameAttr.tile_list.append(self.tile)
                if tile == 2:
                    self.tile = Sprites(x, y, grass_img)
                    self.gameAttr.tile_list.append(self.tile)
                if tile == "x":
                    self.tile = Platform(x, y, platform_img, 1, 0, 50)
                    self.gameAttr.tile_list.append(self.tile)
                    self.gameAttr.platform_group.add(self.tile)
                if tile == "y":
                    self.tile = Platform(x, y, platform_img, 0, 1, 50)
                    self.gameAttr.tile_list.append(self.tile)
                    self.gameAttr.platform_group.add(self.tile)
                if tile == "E":
                    self.tile = Enemy(x, y, 80, ghost, self.gameAttr)
                    self.gameAttr.enemy_sprites.add(self.tile)
                if tile == 8:
                    self.tile = ExitGate(x, y, exit_img)
                    self.gameAttr.ExitsGroup.add(self.tile)
                if tile == 6:
                    self.tile = Coin(x, y, coin_img)
                    self.gameAttr.CoinGroup.add(self.tile)
                self.all_sprites.add(self.tile)
                col_count += 1
            row_count += 1



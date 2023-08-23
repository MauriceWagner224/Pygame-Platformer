import pygame

from worlds import world1, world2
from worldloader import WorldLoader
from properties import *
from interface import InterfaceHandler
from player import Player




## Starting and updating of every main Class, that's needed for the Game
class GameHandler:
    """ init basic pygame parameters and init variables for the Gameloop such as the gamestates Paused/Titlescreen/Mainmenu
        worldnr stores only stores a number which aids in loading the dataset, more details -> reset() function """

    def __init__(self):
        # basic pygame parameters,
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(windows_caption)
        self.main_menu = True
        self.worldnr = 1
        self.current_world_data = None
        self.previousCoins = 0
        # a sprite-groups are dictionaries allows access to multiple sprites at once for example when checking collision
        self.platform_group = pygame.sprite.Group()
        self.missile_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ExitGroup = pygame.sprite.Group()
        self.CoinGroup = pygame.sprite.Group()




    #initiating class instances and spritegroups
    def start(self, map_data, coins=None):
        self.paused = False
        self.handleUI = InterfaceHandler(self.screen)
        self.buttons = self.handleUI.initButtons()
        self.current_world_data = map_data
        # when the next world is loaded, the coins are passed to keep the previous coins
        # when a world is reloaded by playerdeath, no coins are passed, therefore being 0
        if coins != None:
            self.coins = coins
        else:
            self.coins = 0
        # list of world-tiles
        self.tile_list = []

        # pass self as an argument to reference this instance of GameHandler
        self.world = WorldLoader(self, map_data)
        self.player = Player(100, screen_height - 250, self)
        # self.run -> start Gameloop
        self.run()


    """counts up on the worldnr after completing the currentlevel. the number of matchworld is matched to a corresponding worldfile 
        coins are saved in the variable previousCoins, so they ONLY reset(to the amount of the last level) if a level restarts through death/menu
    """
    def nextWorld(self):
        self.worldnr += 1
        self.reset(self.coins)


    """ reset the player and world to load the next world, all spritegroups are cleared
        paused/main
    """
    def reset(self, coins=None):
        self.platform_group.empty()
        self.missile_sprites.empty()
        self.all_sprites.empty()
        self.enemy_sprites.empty()
        self.player_sprites.empty()
        self.ExitGroup.empty()
        self.CoinGroup.empty()

        # worldnr is a counter to help select which worl-data to load
        match self.worldnr:
            case 1:
                self.start(world1.world_data, coins)
            case 2:
                self.start(world2.world_data, coins)
            case 3:
                self.start(world3)




    # actual gameloop
    def run(self):
        while self.run:
            self.clock.tick(fps)
            self.screen.blit(bg_img, (0, 0))
            self.screen.blit(sun_img, (100, 100))
            """ check key input and handle the gamestates and UI elements -> main/paused/death """
            self.handle_gamestate()
            """
            Essential player/world sprites only update if no menu is open
            """
            if self.main_menu == False and self.paused == False and self.player.isdead == False:
                self.gameloop_update()

            pygame.display.flip()

            pygame.display.update()
        pygame.quit()

    """most game-internal updating should happen here"""
    def gameloop_update(self):
        self.player.update()
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pygame.draw.rect(self.screen, (255, 255, 255), self.player.rect, -1)
        self.screen.blit(self.player.image, self.player.rect) # player is drawn
        self.handleUI.drawText(self.coins, self.screen, 25, 20, 32)
        self.handleUI.drawText('Press "P" to pause the Game', self.screen,self.screen.get_width() / 7.5,self.screen.get_height() / 1.075, 16)


    def handle_gamestate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYUP and self.main_menu == False:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
        if self.main_menu:
            if self.handleUI.exit_button.draw(): # Buttons are drawn until clicked --> see Buttonsclass
                self.run = False
            if self.handleUI.start_button.draw():
                self.main_menu = False
        elif self.paused or self.player.isdead:
            if self.paused:
                self.handleUI.drawText('Press "P" to resume the Game', self.screen,self.screen.get_width() / 9.85,self.screen.get_height() / 1.075, 16)
            if self.handleUI.restart_button.draw():
                self.previousCoins = 0
                self.reset()
            if self.handleUI.exit_button.draw():
                self.run = False





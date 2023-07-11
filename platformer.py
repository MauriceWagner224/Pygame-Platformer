import pygame

from worlds import world1, world2
from worldloader import WorldLoader
from properties import *
from interface import UserInterface
from player import Player




## Starting and updating of every main Class, that's needed for the Game
class GameLoop:
	""" init basic pygame parameter and init variables for Gameloop-Conditioning when Pausing etc.
	 	matchworld stores the number when loading a world | currentworld stores the actual map_data and is determined by matchworld"""

	def __init__(self):
		# basic pygame parameters,
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		pygame.display.set_caption(windows_caption)
		# init. gameloop-vars to condition breakpoints when pausing, dying etc.

		self.matchworld = 1
		self.previousCoins = 0


	# actual gameloop
	def run(self):
		while self.run:
			self.clock.tick(fps)
			self.screen.blit(bg_img, (0, 0))
			self.screen.blit(sun_img, (100, 100))


			""" If conditions stops updating of the game-elements, when paused or dead, only background image above is drawn+keyinput"""
			if self.main_menu:
				if self.userInterface.exit_button.draw():
					self.run = False
				if self.userInterface.start_button.draw():
					self.main_menu = False
			elif self.paused:
				if self.userInterface.restart_button.draw():
					self.reset()
				if self.userInterface.exit_button.draw():
					self.run = False
			elif self.player.isdead:
				if self.userInterface.restart_button.draw():
					self.reset()

					#self.start(self.currentworld)
			else:
				self.update()

			"""
			Another conditioned method, that should always be active, no matter the gamestate
			Instructions to pause/resume the game, that are using the same function as the coins, shown in the top left corner. Because of Text size and position on screen.
			the x and y pos are fractions of screenwidth/screenheight 
			"""
			if self.paused:
				self.userInterface.drawText('Press "P" to resume the Game', self.screen,self.screen.get_width() / 9.85,self.screen.get_height() / 1.075, 16)
			else:
				self.userInterface.drawText('Press "P" to pause the Game', self.screen,self.screen.get_width() / 7.5,self.screen.get_height() / 1.075, 16)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				if event.type == pygame.KEYUP and self.main_menu ==  False:
					if event.key == pygame.K_p:
						self.paused = not self.paused

			pygame.display.update()
		# when run == False, pygame.quit event
		pygame.quit()


	""" initiating class instances, sprite-groups, a list containing the world_data tiles
		then run gameloop
	"""
	def start(self, map_data, coins = None):
		self.paused = False
		self.main_menu = True
		self.userInterface = UserInterface(self.screen)
		self.userInterface.initButtons()
		self.currentworld = map_data
		# when the next world is loaded, the coins are passed to keep the previous coins
		# when a world is reloaded, no coins are passed, therefore being 0
		if coins != None:
			self.coins += coins
		else:
			self.coins = 0
		# spritegroups for accessing multiple sprite-instances at once
		self.platform_group = pygame.sprite.Group()
		self.missile_sprites = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		self.player_sprites = pygame.sprite.Group()
		self.ExitsGroup = pygame.sprite.Group()
		self.CoinGroup = pygame.sprite.Group()
		# list of world-tiles
		self.tile_list = []

		# reference this instance of Game() to grand world and player access to Gameclass-vars
		self.world = WorldLoader(self, map_data)
		self.player = Player(100, screen_height - 250, self)
		self.run()


	""" nextWorld counts up the variable(matchworld) after completing the currentlevel. the number of matchworld is matched to a corresponding worldfile 
		coins are saved in the variable previousCoins, so they ONLY reset(to the amount of the last level) if a level restartet through death/menu
	"""
	def nextWorld(self):
		self.matchworld += 1
		self.reset(self.coins)

	""" resets the player and world to load the next world, instances are deleted and spritegroups cleared
		paused/main
	"""
	def reset(self, coins = None):
		self.platform_group.empty()
		self.missile_sprites.empty()
		self.all_sprites.empty()
		self.enemy_sprites.empty()
		self.player_sprites.empty()
		self.ExitsGroup.empty()
		self.CoinGroup.empty()
		del self.userInterface.exit_button
		del self.userInterface.restart_button
		del self.userInterface.start_button
		del self.enemy_sprites
		del self.currentworld
		del self.tile_list
		del self.world
		del self.player
		self.coins = 0

		# matchworld stores a number, that is matched in a switch/case-statement to load the  mapdata of currentworld or the next world to load
		match self.matchworld:
			case 1:
				self.start(world1.world_data, self.previousCoins)
			case 2:
				self.start(world2.world_data, self.previousCoins)
			case 3:
				self.start(world3)


	"""most game-internal updating should happen here"""
	def update(self):
		self.player.update()
		self.all_sprites.update()
		self.all_sprites.draw(self.screen)
		self.userInterface.drawText(self.coins, self.screen, 25, 20, 32)


	def quit(self):
		pygame.quit()



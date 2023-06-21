import pygame.math

from properties import *
from interface import Button, UserInterface
from sprites import Player, World
from maps.map import map_data

class Game():
	def __init__(self):
		# basic pygame parameters
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		pygame.display.set_caption(windows_caption)
		# gameloop-vars to condition pausing and breakpoints
		self.paused = False
		self.main_menu = True

		# spritegroups for overlapping usage in multiple classes (or python classes integrated like an interface in other OOP)
		self.platform_group = pygame.sprite.Group()
		self.missile_sprites = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		self.player_sprites = pygame.sprite.Group()
		# list of world-tiles
		self.tile_list = []
		# initiating instances of basic classes
		self.userInterface = UserInterface(self.screen)
		# reference to this instance of Game() is passed as an argument to access mutable values
		self.world = World(self)
		self.player = Player(100, screen_height - 250, self)


	def run(self):
		# actual gameloop
		while self.run:
			self.clock.tick(fps)
			self.screen.blit(bg_img, (0, 0))
			self.screen.blit(sun_img, (100, 100))


			# conditioning game-updating and drawing to pause/skip as long as the overlay/buttons/menu is open
			if self.main_menu:
				if self.userInterface.exit_button.draw():
					run = False
				if self.userInterface.start_button.draw():
					self.main_menu = False
			elif self.paused:
				if self.userInterface.resume_button.draw():
					self.paused = not self.paused
			elif self.player.isdead():
				if self.userInterface.restart_button.draw():
					self.quit()
					self.__init__()
					self.start()
			else:
				self.update()

			try:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.quit()
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_p:
							self.paused = not self.paused
			except KeyboardInterrupt:
				pass
			pygame.display.update()
		self.quit()


	def start(self):
		self.userInterface.initButtons()
		self.run()

	def update(self):
		self.world.update()
		self.player.update()
		pygame.display.update()

	def quit(self):
		self.run = False
		pygame.quit()





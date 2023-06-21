from properties import *

# parent class with basic params that are in common with it's child
class UserInterface():
	def __init__(self, screen):
		self.screen = screen

	def initButtons(self):
		# create buttons
		self.restart_button = Button(self.screen, screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
		self.start_button = Button(self.screen, screen_width // 2 - 350, screen_height // 2, start_img)
		self.exit_button = Button(self.screen, screen_width // 2 + 100, screen_height // 2, exit_img)
		self.resume_button = Button(self.screen, screen_width // 2, screen_height // 2, load_img)


class Button(object):
	def __init__(self, screen, x, y, image):
		self.screen = screen
		self.clicked = False
		self.action = False
		self.image = image
		self.rect = self.image.get_rect()
		self.image = image
		self.rect.x = x
		self.rect.y = y

	def draw(self):
		self.action = False

		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				self.action = True
		if not pygame.mouse.get_pressed()[0]:
			self.action = False

		# draw button
		self.screen.blit(self.image, self.rect)

		return self.action

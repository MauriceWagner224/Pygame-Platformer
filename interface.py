import pygame

from properties import *

# parent class with basic params it has in common with it's children
class InterfaceHandler():
	def __init__(self, screen):
		self.screen = screen

	def initButtons(self):
		# create buttons
		self.restart_button = Button(self.screen, screen_width // 2 -restart_img.get_width()/2, screen_height // 2, restart_img)
		self.start_button = Button(self.screen, screen_width // 2 - start_img.get_width()/2, screen_height // 2, start_img)
		self.exit_button = Button(self.screen, screen_width // 2 - exit_btn.get_width()/2, screen_height // 2 + 150, exit_btn)
		return self

	def drawText(self, text, screen, width, height, size):
		# load custom font
		font = pygame.font.Font("font/MMRock9.ttf", size)
		self.text = font.render(str(text), True, (10, 10, 10))
		self.width = self.text.get_width() + width
		self.height = self.text.get_height() + height
		screen.blit(self.text, (self.width, self.height))


class Button(object):
	def __init__(self, screen, x, y, image):
		self.screen = screen
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

		# when the button is drawn, check if mousebutton got pressed and is colliding with the cursor
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				self.action = True
		if not pygame.mouse.get_pressed()[0]:
			self.action = False

		# draw button
		self.screen.blit(self.image, self.rect)

		return self.action





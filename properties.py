import pygame

fps = 60

# define gamewindow/size properties
screen_width = 1000
screen_height = 800
rows = 20
tile_size = screen_height / 20
tile_size_y = screen_height/ rows
tile_size_x = screen_width / rows
windows_caption = "Tolles Spiel"


#movement-consts
friction = -0.18
gravity = 0.8

# load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
restart_img = pygame.image.load('img/restart_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
load_img = pygame.image.load('img/load_btn.png')
dirt_img = pygame.image.load('img/dirt.png')
grass_img = pygame.image.load('img/grass.png')
platform_img = pygame.image.load('img/platform.png')
player_img_right1 = pygame.image.load(f'img/guy1.png')
player_img_right1 = pygame.transform.scale(player_img_right1, (screen_height / 16, screen_width / 16))
enemy_img = pygame.image.load('img/enemy.png')
missile_img = pygame.image.load('img/pew.png')

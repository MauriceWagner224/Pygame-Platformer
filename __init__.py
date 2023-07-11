from platformer import GameLoop
from worlds import world1, world2

class StartGame(object):
    def __init__(self):
        game = GameLoop()
        game.start(world1.world_data)


g = StartGame()




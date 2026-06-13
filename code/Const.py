# C
import pygame

COLOR_YELLOW = (255, 254, 9)
COLOR_WHITE = (255, 255, 255)


# E
EVENT_POINT = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player2': 3,
    'Point': 2,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - Cooperative',
               'NEW GAME 2P - Cooperative',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}

#S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
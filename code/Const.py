# C
import pygame

COLOR_YELLOW = (255, 254, 9)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


# E
EVENT_POINT = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level3Bg4': 4,
    'Level3Bg5': 5,
    'Level3Bg6': 6,
    'Level3Bg7': 7,
    'Player1': 3,
    'Player2': 3,
    'Point': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Level3Bg5': 999,
    'Level3Bg6': 999,
    'Level3Bg7': 999,
    'Player1': 300,
    'Player2': 300,
    'Point': 50,

}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - Cooperative',
               'NEW GAME 2P - Competitive',
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
SPAWN_TIME = 550

# T
TIMEOUT_STEP = 1000 # 1s
TIMEOUT_LEVEL = 20000 #20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
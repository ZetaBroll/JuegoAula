##  C  ##
import pygame


C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)



##  E  ##
EVENT_ENEMY = pygame.USEREVENT + 1  # Custom event for spawning enemies
ENTITY_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 6,
    "Player1": 5,
    "Player2": 5,
    "Enemy1": 2,
    "Enemy2": 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Player1': 200,
    'Player1Shot': 1,
    'Player2': 200,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 75,
    'Enemy2Shot': 1,
}


##  M  ##
MENU_OPTION = (
    "NEW GAME 1P",
    "NEW GAME 2P - COOPERATIVE",
    "NEW GAME 2P - COOPERATIVE",
    "SCORE",
    "EXIT")



##  P  ##

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_LSHIFT,
                    'Player2': pygame.K_RSHIFT}


##  S  ##
SPAWN_TIME = 2500

##  W  ##
WIN_WIDTH= 576
WIN_HEIGHT= 324



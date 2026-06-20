import sys
from typing import Any

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # If the user chose a game option (Single, Co-op, etc.)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] # Player1, Player2

                # List of levels to go through
                level_names = ['Level1', 'Level2', 'Level3']

                for name in level_names:
                    level = Level(self.window, name, menu_return, player_score)
                    level_finished = level.run(player_score)

                    # If the level did not end successfully (e.g., the player died), stop the loop.
                    if not level_finished:
                        break

            # If the user chose to exit
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()


import pygame
import sys
from code.Menu import Menu
from code.Level import Level
from code.Score import Score
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]

                # Executes the levels sequentially
                for name in ['Level1', 'Level2', 'Level3']:
                    level = Level(self.window, name, menu_return, player_score)
                    level_finished = level.run(player_score)
                    if not level_finished:
                        break  #If you lose, the level loop ends.

                # After the levels, go to the Score.
                score = Score(self.window)
                score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:  # Score
                score = Score(self.window)
                score.show()

            elif menu_return == MENU_OPTION[4]: # To go out
                pygame.quit()
                sys.exit()
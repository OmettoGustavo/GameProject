import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font
from datetime import datetime
from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)

        names = ["", ""]
        current_player = 0
        is_2p = game_mode in [MENU_OPTION[1], MENU_OPTION[2]]

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!', COLOR_YELLOW, SCORE_POS['Title'])
            self.score_text(24, f'P1 Score: {player_score[0]}', COLOR_YELLOW, (400, 200))
            if is_2p:
                self.score_text(24, f'P2 Score: {player_score[1]}', COLOR_YELLOW, (400, 240))

            prompt = f'Player {current_player + 1} - Name (4 chars): {names[current_player]}'
            self.score_text(24, prompt, COLOR_YELLOW, (400, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(names[current_player]) > 0:
                        if is_2p and current_player == 0:
                            current_player = 1
                        else:
                            db = DBProxy('DBScore.db')
                            db.save({'name': names[0], 'score': player_score[0],
                                     'date': datetime.now().strftime("%d/%m/%Y")})
                            if is_2p:
                                db.save({'name': names[1], 'score': player_score[1],
                                         'date': datetime.now().strftime("%d/%m/%Y")})
                            db.close();
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        names[current_player] = names[current_player][:-1]
                    elif len(names[current_player]) < 4 and event.unicode.isalnum():
                        names[current_player] += event.unicode.upper()
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db = DBProxy('DBScore.db')
        top10 = db.retrieve_top10()
        db.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'TOP 10 SCORES', COLOR_YELLOW, SCORE_POS['Title'])
            for i, entry in enumerate(top10):
                texto = f"{i + 1} - {entry[0]} : {entry[1]} ({entry[2]})"
                self.score_text(22, texto, COLOR_YELLOW, (400, 150 + (i * 35)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            pygame.display.flip()

    def score_text(self, text_size, text, text_color, text_center_pos):
        font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)
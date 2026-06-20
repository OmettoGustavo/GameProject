import sys
import pygame
from pygame import Surface

from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_POINT, SPAWN_TIME, ENTITY_SPEED, COLOR_GREEN, \
    COLOR_BLUE, TIMEOUT_STEP, EVENT_TIMEOUT, TIMEOUT_LEVEL, COLOR_YELLOW
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        # Player 1
        temp_players = EntityFactory.get_entity('Player1')
        player1 = temp_players[0]
        player1.score = player_score[0]
        self.entity_list.append(player1)

        # Player 2 (if needed)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            temp_players2 = EntityFactory.get_entity('Player2')
            player2 = temp_players2[0]
            player2.score = player_score[1]
            self.entity_list.append(player2)

        pygame.time.set_timer(EVENT_POINT, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            # Draw and move entities
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(ENTITY_SPEED)

                if isinstance(ent, Player):
                    color = COLOR_GREEN if ent.name == 'Player1' else COLOR_YELLOW
                    pos_health = (10, 25) if ent.name == 'Player1' else (10, 45)
                    pos_score = (250, 5) if ent.name == 'Player1' else (400, 5)

                    self.level_text(14, f'{ent.name} - Health: {ent.health}', color, pos_health)
                    self.level_text(14, f'{ent.name} Score: {ent.score}', color, pos_score)

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_POINT:

                    self.entity_list.append(EntityFactory.get_entity('Point'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        self.update_player_scores(player_score)
                        self.reset_timers()
                        return True

            # Check if players are still alive
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
            if not found_player:
                self.reset_timers()
                return False

            # UI and Updates
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            pygame.display.flip()

            # Physical
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def update_player_scores(self, player_score: list[int]):
        for ent in self.entity_list:
            if isinstance(ent, Player):
                if ent.name == 'Player1':
                    player_score[0] = ent.score
                if ent.name == 'Player2':
                    player_score[1] = ent.score

    def reset_timers(self):
        pygame.time.set_timer(EVENT_POINT, 0)
        pygame.time.set_timer(EVENT_TIMEOUT, 0)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)

        # Renders the main text and the outline (black)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        outline_surf = text_font.render(text, True, (0, 0, 0)).convert_alpha()

        # Thinner outline: only 1 pixel offset on the diagonals
        offsets = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

        # Draw the outline
        for dx, dy in offsets:
            self.window.blit(outline_surf, (text_pos[0] + dx, text_pos[1] + dy))

        # Draw the main text over it.
        self.window.blit(text_surf, text_pos)
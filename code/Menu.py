
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option_index = 0  # Índice para controlar a seleção

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "Bee's", COLOR_YELLOW, ((WIN_WIDTH / 2), 70))
            self.menu_text(80, "Bounty", COLOR_YELLOW, ((WIN_WIDTH / 2), 120))

            # Desenha as opções com destaque para a selecionada
            for i in range(len(MENU_OPTION)):
                color = COLOR_YELLOW if i == self.menu_option_index else COLOR_WHITE
                self.menu_text(20, MENU_OPTION[i], color, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            self.menu_option_index = (self.menu_option_index + 1) % len(MENU_OPTION)
                        elif event.key == pygame.K_UP:
                            self.menu_option_index = (self.menu_option_index - 1) % len(MENU_OPTION)
                        elif event.key == pygame.K_RETURN:
                            return MENU_OPTION[self.menu_option_index] # Retorna a string selecionada

    def menu_text(self, text_size, text, text_color, text_center_pos):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Point import Point


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg0':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return [Player('Player1', (10, WIN_HEIGHT / 2 - 30))] # Retorna lista
            case 'Player2':
                return [Player('Player2', (10, WIN_HEIGHT / 2 + 30))] # Retorna lista
            case 'Point':
                return Point('Point', (WIN_WIDTH +10, random.randint(40, WIN_HEIGHT - 40)))
            case _:
                return [] # Retorno padrão (lista vazia)

from code import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1BG{i}', (0,0)))
                    list_bg.append(Background(f'Level1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player(f'Player1', (10, WIN_HEIGHT / 2))


from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Point(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ENTITY_SPEED=None):
        self.rect.centerx -= ENTITY_SPEED[self.name]
from code.Entity import Entity
from code.Player import Player
from code.Point import Point

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity, entity_list: list[Entity]):
        if isinstance(ent, Point):
            if ent.rect.right < 0:
                ent.health = 0
                # Applies damage to all living players on the screen.
                for player in entity_list:
                    if isinstance(player, Player):
                        player.health -= 10 # Define the damage value

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if ent1.rect.colliderect(ent2.rect):
            # Logic for collision between Player and Point
            if isinstance(ent1, Player) and isinstance(ent2, Point):
                ent1.score += 10
                ent2.health = 0
            elif isinstance(ent1, Point) and isinstance(ent2, Player):
                ent2.score += 10
                ent1.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            # We went through the entire list to check who is alive.
            EntityMediator.__verify_collision_window(entity1, entity_list)

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):

        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)
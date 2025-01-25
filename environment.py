import random

from entities import Entity
from config import Config as c


class Environment:
    def __init__(self, width, height, num_entities):
        self.width = width
        self.height = height
        self.entities = [
            Entity(
                x=random.randint(0, width),
                y=random.randint(0, height),
                speed=c.ENTITY_SPEED,
                size=c.ENTITY_SIZE,
            )
            for _ in range(num_entities)
        ]

    def update(self):
        for entity in self.entities:
            entity.move(self.width, self.height)
            for other in self.entities:
                if entity != other:
                    entity.eat(other)

        # Remove dead entities
        self.entities = [e for e in self.entities if e.alive]

        # # Add new entities if reproduction occurs
        # new_entities = []
        # for entity in self.entities:
        #     new_entity = entity.reproduce()
        #     if new_entity:
        #         new_entities.append(new_entity)
        
        # self.entities.extend(new_entities)

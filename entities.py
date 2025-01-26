import random
from constants import Colors

class Entity:
    def __init__(self, x, y, speed, level):
        self.x = x
        self.y = y
        self.speed = speed
        self.level = level
        self.alive = True
        self.color = Colors.LEVELS[level-1]

    def move(self, box_width, box_height):
        self.x += random.choice([-1, 0, 1]) * self.speed
        self.y += random.choice([-1, 0, 1]) * self.speed
        self.x = max(0, min(self.x, box_width - self.level))
        self.y = max(0, min(self.y, box_height - self.level))

    def check_collision(self, other_entity):
        return (abs(self.x - other_entity.x) < self.level and 
                abs(self.y - other_entity.y) < self.level)

    def interact(self, other_entity: 'Entity'):
        if self.check_collision(other_entity):
            if self.level > other_entity.level: 
                self.eat_other(other_entity) # This entity eats the other entity
            elif self.level < other_entity.level:
                self.get_eaten(other_entity) # This entity gets eaten by the other entity
            else:
                random.choice([self.eat_other, self.get_eaten])(other_entity) # Randomly choose who eats who

    def eat_other(self, other_entity: 'Entity'):
        other_entity.alive = False # The other entity dies
        self.level_up() # This entity grows
            
    def get_eaten(self, other_entity: 'Entity'):
        self.alive = False  # This entity dies
        other_entity.level_up()  # The other entity grows

    def level_up(self):
        self.level += 1
        self.level = min(self.level, len(Colors.LEVELS))
        self.color = Colors.LEVELS[self.level-1]

    # def reproduce(self):
    #     if random.random() < 0.01:  # Small chance to reproduce
    #         return Entity(self.x + 2, self.y + 2, self.speed, self.level)

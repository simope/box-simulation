import random

class Entity:
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.alive = True

    def move(self, box_width, box_height):
        self.x += random.choice([-1, 0, 1]) * self.speed
        self.y += random.choice([-1, 0, 1]) * self.speed
        self.x = max(0, min(self.x, box_width - self.size))
        self.y = max(0, min(self.y, box_height - self.size))

    def check_collision(self, other_entity):
        return (abs(self.x - other_entity.x) < self.size and 
                abs(self.y - other_entity.y) < self.size)

    def interact(self, other_entity: 'Entity'):
        if self.check_collision(other_entity):
            if self.size > other_entity.size: 
                self.eat_other(other_entity) # This entity eats the other entity
            elif self.size < other_entity.size:
                self.get_eaten(other_entity) # This entity gets eaten by the other entity
            else:
                random.choice([self.eat_other, self.get_eaten])(other_entity) # Randomly choose who eats who

    def eat_other(self, other_entity: 'Entity'):
        other_entity.alive = False # The other entity dies
        self.size += 1 # This entity grows
            
    def get_eaten(self, other_entity: 'Entity'):
        self.alive = False  # This entity dies
        other_entity.size += 1  # The other entity grows

    # def reproduce(self):
    #     if random.random() < 0.01:  # Small chance to reproduce
    #         return Entity(self.x + 2, self.y + 2, self.speed, self.size)

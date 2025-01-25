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

    def eat(self, other_entity: 'Entity'):
        if self.check_collision(other_entity):
            other_entity.alive = False  # 'Eat' the other entity
            self.size += 1  # Grow after eating

    def reproduce(self):
        if random.random() < 0.01:  # Small chance to reproduce
            return Entity(self.x + 2, self.y + 2, self.speed, self.size)

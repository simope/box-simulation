import pygame
from environment import Environment
from config import Config as c

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((c.BOX_WIDTH, c.BOX_HEIGHT))
    clock = pygame.time.Clock()
    env = Environment(c.BOX_WIDTH, c.BOX_HEIGHT, c.NUM_ENTITIES)

    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.update()
        
        for entity in env.entities:
            pygame.draw.circle(screen, (255, 0, 0), (entity.x, entity.y), entity.size)
        
        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

import pygame
from environment import Environment
from config import Config as c
from constants import Colors

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((c.BOX_WIDTH, c.BOX_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)
    env = Environment(c.BOX_WIDTH, c.BOX_HEIGHT, c.NUM_ENTITIES)

    running = True
    while running:
        screen.fill(Colors.MY_GREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.update()
        env.render_dashboard(screen, font)

        for entity in env.entities:
            pygame.draw.circle(screen, Colors.GREEN, (entity.x, entity.y), entity.size)
        
        pygame.display.flip()
        clock.tick(c.FPS)

    pygame.quit()

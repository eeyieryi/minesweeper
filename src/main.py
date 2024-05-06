import pygame

from config import Config
from minesweeper import Minesweeper


def run():
    config = Config()

    screen = pygame.display.set_mode((config.window_width, config.window_height))
    pygame.display.set_caption(config.window_title)
    clock = pygame.time.Clock()

    game = Minesweeper(config)

    font = pygame.font.SysFont("monospace", 26)

    while game.is_running():
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.kill()
            if event.type == pygame.KEYDOWN:
                game.handle_keydown_events(event.key)

        # draw to screen
        screen.fill("black")
        game.draw(screen, font)

        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

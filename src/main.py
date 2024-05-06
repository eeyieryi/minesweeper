import pygame

from config import Config
from minesweeper import Minesweeper


def run():
    config = Config()

    screen_surface = pygame.display.set_mode(
        (config.window_width, config.window_height)
    )
    pygame.display.set_caption(config.window_title)
    clock = pygame.time.Clock()

    game = Minesweeper(config)

    while game.is_running():
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.kill()
            elif event.type == pygame.KEYDOWN:
                game.handle_keydown_events(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_mousedown_event(event)

        # draw to screen
        screen_surface.fill("black")
        game.draw(screen_surface)

        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

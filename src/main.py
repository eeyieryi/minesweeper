import pygame

from constants import GAME_TITLE, WINDOW_SIZE
from minesweeper import Minesweeper


def run():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    game = Minesweeper()

    while game.is_running():
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.kill()
            if event.type == pygame.KEYDOWN:
                game.handle_keydown_events(event.key)

        # draw to screen
        screen.fill("black")
        game.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

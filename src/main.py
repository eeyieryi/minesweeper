import pygame

from constants import GAME_TITLE, GRID_SIZE, WINDOW_SIZE
from grid import Grid
from selection import Selection


def run():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    running = True

    grid = Grid(size=GRID_SIZE)
    selection = Selection()

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_h:
                    selection.go_left()
                if event.key == pygame.K_l:
                    selection.go_right()
                if event.key == pygame.K_k:
                    selection.go_up()
                if event.key == pygame.K_j:
                    selection.go_down()

        # draw to screen
        screen.fill("black")
        grid.draw(screen)
        selection.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)
        # running = False


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

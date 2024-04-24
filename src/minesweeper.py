import pygame

from constants import GRID_SIZE
from grid import Grid
from selection import Selection


class Minesweeper:
    def __init__(self) -> None:
        self._grid = Grid(size=GRID_SIZE)
        self._selection = Selection()
        self._running = True

    def handle_keydown_events(self, key: int) -> None:
        if key == pygame.K_q:
            self.kill()
        elif key == pygame.K_h:
            self._selection.go_left()
        elif key == pygame.K_l:
            self._selection.go_right()
        elif key == pygame.K_k:
            self._selection.go_up()
        elif key == pygame.K_j:
            self._selection.go_down()

    def draw(self, screen: pygame.Surface) -> None:
        self._grid.draw(screen)
        self._selection.draw(screen)

    def is_running(self):
        return self._running

    def kill(self):
        self._running = False

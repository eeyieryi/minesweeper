import pygame

from config import Config
from grid import Grid
from selection import Selection
from ui import Ui


class Minesweeper:
    def __init__(self, config: Config) -> None:
        self._cfg = config
        self._setup()

    def _setup(self) -> None:
        self._selection = Selection(self._cfg)
        self._ui = Ui(self._cfg, self._selection)
        self._grid = Grid(self._cfg)
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
        elif key == pygame.K_SPACE:
            self._grid.toggle_flag_at(self._selection.get_coords())
        elif key == pygame.K_RETURN:
            self._grid.trigger_cell_at(self._selection.get_coords())

    def draw(self, surface) -> None:
        self._ui.draw(surface, self._grid)

    def is_running(self) -> bool:
        return self._running

    def kill(self) -> None:
        self._running = False

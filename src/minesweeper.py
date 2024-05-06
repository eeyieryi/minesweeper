import pygame

from cell import CellState
from config import Config
from grid import Grid
from selection import Selection
from utils import Utils


class Minesweeper:
    def __init__(self, config: Config) -> None:
        self._cfg = config
        self._selection = Selection(self._cfg)
        self._utils = Utils(self._cfg, self._selection)

        self.new_game()

    def new_game(self) -> None:
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
            self._grid.toggle_flag(self._selection.get_coords())
        elif key == pygame.K_RETURN:
            self._grid.trigger_cell(self._selection.get_coords())

    def draw(self, surface: pygame.Surface, font) -> None:
        img = font.render(self._grid.get_state().name, True, (255, 0, 0))
        surface.blit(img, (20, 20))
        for cell in self._grid._cells:
            cell_state = cell.get_state()
            cell_label = cell.get_label()
            x, y = self._utils.get_cell_screen_pos(cell.get_coords())
            if cell_state == CellState.UNOPENED:
                pygame.draw.rect(
                    surface,
                    "grey",
                    pygame.Rect(
                        x,
                        y,
                        self._cfg.grid_cell_size - 1,
                        self._cfg.grid_cell_size - 1,
                    ),
                )
            elif cell_state == CellState.FLAGGED:
                pygame.draw.rect(
                    surface,
                    "red",
                    pygame.Rect(
                        x + 3,
                        y + 3,
                        self._cfg.grid_cell_size - 6,
                        self._cfg.grid_cell_size - 6,
                    ),
                )
            elif cell_state == CellState.OPENED:
                if cell in self._grid._mines:
                    pygame.draw.circle(
                        surface,
                        "white",
                        (
                            x + self._cfg.grid_cell_size / 2,
                            y + self._cfg.grid_cell_size / 2,
                        ),
                        7,
                    )
                else:
                    img = font.render(cell_label, True, (255, 0, 0))
                    surface.blit(img, (x + 3, y + 3))
        pygame.draw.circle(
            surface,
            "green",
            self._utils.get_selection_screen_pos(),
            5,
        )

    def is_running(self):
        return self._running

    def kill(self):
        self._running = False

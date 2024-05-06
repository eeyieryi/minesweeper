import pygame

from cell import CellState
from config import Config
from grid import Grid
from selection import Selection


class Minesweeper:
    def __init__(self, config: Config) -> None:
        self.cfg = config
        self.new_game()

    def new_game(self) -> None:
        self._grid = Grid(self.cfg)
        self._selection = Selection(self.cfg)
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

    def get_cell_screen_pos(self, coords: tuple[int, int]) -> tuple[float, float]:
        grid_num_rows, grid_num_cols = self._grid.get_size()

        row_index = coords[0] % grid_num_rows
        col_index = coords[1] % grid_num_cols

        return (
            self.cfg.grid_margin_left + col_index * self.cfg.grid_cell_size,
            self.cfg.grid_margin_top + row_index * self.cfg.grid_cell_size,
        )

    def get_selection_screen_pos(self, coords: tuple[int, int]) -> tuple[float, float]:
        cell_coords = self.get_cell_screen_pos(coords)
        return (
            cell_coords[0] + self.cfg.grid_cell_size / 2,
            cell_coords[1] + self.cfg.grid_cell_size / 2,
        )

    def draw(self, surface: pygame.Surface, font) -> None:
        img = font.render(self._grid.get_state().name, True, (255, 0, 0))
        surface.blit(img, (20, 20))
        for cell in self._grid._cells:
            cell_state = cell.get_state()
            cell_label = cell.get_label()
            x, y = self.get_cell_screen_pos(cell.get_coords())
            if cell_state == CellState.UNOPENED:
                pygame.draw.rect(
                    surface,
                    "grey",
                    pygame.Rect(
                        x,
                        y,
                        self.cfg.grid_cell_size - 1,
                        self.cfg.grid_cell_size - 1,
                    ),
                )
            elif cell_state == CellState.FLAGGED:
                pygame.draw.rect(
                    surface,
                    "red",
                    pygame.Rect(
                        x + 3,
                        y + 3,
                        self.cfg.grid_cell_size - 6,
                        self.cfg.grid_cell_size - 6,
                    ),
                )
            elif cell_state == CellState.OPENED:
                if cell in self._grid._mines:
                    pygame.draw.circle(
                        surface,
                        "white",
                        (
                            x + self.cfg.grid_cell_size / 2,
                            y + self.cfg.grid_cell_size / 2,
                        ),
                        7,
                    )
                else:
                    img = font.render(cell_label, True, (255, 0, 0))
                    surface.blit(img, (x + 3, y + 3))
        pygame.draw.circle(
            surface,
            "green",
            self.get_selection_screen_pos(self._selection.get_coords()),
            5,
        )

    def is_running(self):
        return self._running

    def kill(self):
        self._running = False

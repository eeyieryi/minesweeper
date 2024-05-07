import pygame

from config import Config
from game.cell import CellState
from game.grid import Grid
from game_state import GameState
from selection import Selection
from ui.fonts import FontSize, font_filepath


class Ui:
    def __init__(self, cfg: Config, selection: Selection) -> None:
        self._cfg = cfg
        self._selection = selection
        self.fonts = {
            FontSize.Small: pygame.Font(font_filepath, 26),
            FontSize.Medium: pygame.Font(font_filepath, 30),
            FontSize.Large: pygame.Font(font_filepath, 42),
        }

    def draw(self, surface: pygame.Surface, game_state: GameState, grid: Grid) -> None:
        if game_state == GameState.MAIN:
            self.draw_main_menu(surface)
        elif game_state == GameState.PLAYING:
            self.draw_grid_status(surface, grid)
            self.draw_grid(surface, grid)
            self.draw_selection(surface)
        elif game_state == GameState.OVER:
            self.draw_grid_status(surface, grid)
            self.draw_grid(surface, grid)

    def draw_grid_status(self, surface: pygame.Surface, grid: Grid) -> None:
        img = self.fonts[FontSize.Medium].render(
            grid.get_state().name, True, (255, 0, 0)
        )
        surface.blit(img, (20, 20))

    def draw_grid(self, surface: pygame.Surface, grid: Grid) -> None:
        for cell in grid.get_cells():
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
                if cell in grid.get_mines():
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
                    img = self.fonts[FontSize.Medium].render(
                        cell_label, True, (255, 0, 0)
                    )
                    surface.blit(img, (x + 6, y))

    def draw_selection(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(
            surface,
            "green",
            self.get_selection_screen_pos(),
            5,
        )

    def get_cell_screen_pos(self, coords: tuple[int, int]) -> tuple[float, float]:
        row_index = coords[0] % self._cfg.grid_num_rows
        col_index = coords[1] % self._cfg.grid_num_cols

        return (
            self._cfg.grid_margin_left + col_index * self._cfg.grid_cell_size,
            self._cfg.grid_margin_top + row_index * self._cfg.grid_cell_size,
        )

    def get_selection_screen_pos(self) -> tuple[float, float]:
        cell_coords = self.get_cell_screen_pos(self._selection.get_coords())
        return (
            cell_coords[0] + self._cfg.grid_cell_size / 2,
            cell_coords[1] + self._cfg.grid_cell_size / 2,
        )

    def get_coords_from_screen_pos(
        self, pos: tuple[int, int]
    ) -> tuple[int, int] | None:
        pos_x, pos_y = pos

        start_x, start_y = self.get_cell_screen_pos((0, 0))
        end_x, end_y = self.get_cell_screen_pos(
            (self._cfg.grid_num_rows - 1, self._cfg.grid_num_cols - 1)
        )
        end_x += self._cfg.grid_cell_size
        end_y += self._cfg.grid_cell_size

        if pos_x >= start_x and pos_x <= end_x and pos_y >= start_y and pos_y <= end_y:
            row_index = (
                (pos_y - start_y) // self._cfg.grid_cell_size
            ) % self._cfg.grid_num_rows
            col_index = (
                (pos_x - start_x) // self._cfg.grid_cell_size
            ) % self._cfg.grid_num_cols
            return (int(row_index), int(col_index))

    def draw_main_menu(self, surface: pygame.Surface) -> None:
        img = self.fonts[FontSize.Large].render(
            self._cfg.window_title, True, (255, 0, 0)
        )
        surface.blit(img, (240, 200))

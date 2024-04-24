import pygame

from cell import Cell, CellState
from constants import (
    GRID_MARGIN_LEFT,
    GRID_MARGIN_TOP,
    GRID_NUM_COLS,
    GRID_NUM_ROWS,
    TILE_SIZE,
)


class Tile:
    def __init__(self, coords: tuple[int, int], lst_index: int = None) -> None:
        self._cell = Cell()
        self._coords = coords
        self._screen_pos = self.get_screen_pos()
        self._grid_list_index = lst_index

    def get_grid_list_index(self) -> int:
        return self._grid_list_index

    def get_cell_state(self) -> CellState:
        return self._cell.get_state()

    def draw(self, surface: pygame.Surface) -> None:
        cell_state = self._cell.get_state()
        if cell_state == CellState.UNOPENED:
            pygame.draw.rect(
                surface,
                "grey",
                pygame.Rect(
                    self._screen_pos[0],
                    self._screen_pos[1],
                    TILE_SIZE - 1,
                    TILE_SIZE - 1,
                ),
            )
        elif cell_state == CellState.FLAGGED:
            pygame.draw.circle(surface, "red", self._screen_pos, 5)
        elif cell_state == CellState.OPENED:
            pygame.draw.circle(surface, "white", self._screen_pos, 5)

    def get_screen_pos(self) -> tuple[float, float]:
        row_index = self._coords[0] % GRID_NUM_ROWS
        col_index = self._coords[1] % GRID_NUM_COLS

        return (
            GRID_MARGIN_LEFT + col_index * TILE_SIZE,
            GRID_MARGIN_TOP + row_index * TILE_SIZE,
        )

    def __repr__(self) -> str:
        return f"Tile(coords=({self._coords[0]}, {self._coords[1]}))"

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
    def __init__(self, pos: tuple[float, float]) -> None:
        self._pos = pos
        self._cell = Cell()

    def get_cell_state(self) -> CellState:
        return self._cell.get_state()

    def draw(self, surface: pygame.Surface):
        cell_state = self._cell.get_state()
        if cell_state == CellState.UNOPENED:
            pygame.draw.rect(
                surface,
                "grey",
                pygame.Rect(self._pos[0], self._pos[1], TILE_SIZE - 1, TILE_SIZE - 1),
            )
        elif cell_state == CellState.FLAGGED:
            pygame.draw.circle(surface, "red", self._pos, 5)
        elif cell_state == CellState.OPENED:
            pygame.draw.circle(surface, "white", self._pos, 5)
        pass

    def __repr__(self) -> str:
        return f"Tile(pos=({self._pos[0]}, {self._pos[1]}))"


def get_tile_pos(row_i: int, column_i: int) -> tuple[float, float]:
    row_index = row_i % GRID_NUM_ROWS
    col_index = column_i % GRID_NUM_COLS
    tile_pos = (
        GRID_MARGIN_LEFT + col_index * TILE_SIZE,
        GRID_MARGIN_TOP + row_index * TILE_SIZE,
    )
    return tile_pos

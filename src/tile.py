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
    def __init__(self, coords: tuple[int, int]) -> None:
        self._cell = Cell()
        self._coords = coords
        self._screen_pos = self.get_screen_pos()

    def toggle_flag_mark(self) -> None:
        cell_state = self.get_cell_state()
        if cell_state == CellState.UNOPENED:
            self._cell.change_state_to(CellState.FLAGGED)
        elif cell_state == CellState.FLAGGED:
            self._cell.change_state_to(CellState.UNOPENED)
        else:
            raise Exception("Cannot (un)flag an open cell")

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
            pygame.draw.rect(
                surface,
                "red",
                pygame.Rect(
                    self._screen_pos[0] + 3,
                    self._screen_pos[1] + 3,
                    TILE_SIZE - 6,
                    TILE_SIZE - 6,
                ),
            )
        elif cell_state == CellState.OPENED:
            pygame.draw.rect(
                surface,
                "white",
                pygame.Rect(
                    self._screen_pos[0] + 3,
                    self._screen_pos[1] + 3,
                    TILE_SIZE - 6,
                    TILE_SIZE - 6,
                ),
            )

    def get_screen_pos(self) -> tuple[float, float]:
        row_index = self._coords[0] % GRID_NUM_ROWS
        col_index = self._coords[1] % GRID_NUM_COLS

        return (
            GRID_MARGIN_LEFT + col_index * TILE_SIZE,
            GRID_MARGIN_TOP + row_index * TILE_SIZE,
        )

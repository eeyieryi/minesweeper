import pygame

from constants import GRID_NUM_COLS
from tile import Tile


class Grid:
    def __init__(self, size: tuple[int, int]) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._tiles = self.make_empty_grid_tiles()

    def make_empty_grid_tiles(self) -> list[Tile]:
        tiles: list[Tile] = []
        row_index, col_index = 0, 0
        for lst_index in range(self._num_rows * self._num_cols):
            coords = (row_index, col_index)
            tile = Tile(coords, lst_index)
            tiles.append(tile)
            if col_index + 1 == GRID_NUM_COLS:
                row_index += 1  # down one row
                col_index = 0  # reset column
            else:
                col_index += 1  # go to the next column
        return tiles

    def get_tiles(self) -> list[Tile]:
        return self._tiles

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

    def draw(self, surface: pygame.Surface) -> None:
        for tile in self._tiles:
            tile.draw(surface)

    def __repr__(self) -> str:
        return f"Grid(size=({self._num_rows}, {self._num_cols}))"

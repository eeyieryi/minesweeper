import pygame

from constants import GRID_NUM_COLS
from tile import Tile, get_tile_pos


class Grid:
    def __init__(self, size: tuple[int, int]) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._tiles = self.make_empty_grid_tiles()

    def make_empty_grid_tiles(self) -> list[Tile]:
        tiles: list[Tile] = []
        row_i, col_i = 0, 0
        for _ in range(self._num_rows * self._num_cols):
            tile = Tile(pos=get_tile_pos(row_i, col_i))
            tiles.append(tile)
            if col_i + 1 == GRID_NUM_COLS:
                row_i += 1  # down one row
                col_i = 0  # reset column
            else:
                col_i += 1  # go to the next column
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

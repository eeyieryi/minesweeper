import pygame

from selection import Selection
from tile import Tile


class Grid:
    def __init__(self, size: tuple[int, int]) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._tiles = self.make_empty_grid_tiles()

    def make_empty_grid_tiles(self) -> list[Tile]:
        tiles: list[Tile] = []
        row_index, col_index = 0, 0
        for _ in range(self._num_rows * self._num_cols):
            coords = (row_index, col_index)
            tile = Tile(coords)
            tiles.append(tile)
            if col_index + 1 == self._num_cols:
                row_index += 1  # down one row
                col_index = 0  # reset column
            else:
                col_index += 1  # go to the next column
        return tiles

    def toggle_flag_mark(self, selection: Selection):
        selection_coords = selection.get_coords(self.get_size())
        self._tiles[self.get_tile_index(selection_coords)].toggle_flag_mark()

    def get_tile_index(self, coords: tuple[int, int]) -> int:
        return (coords[0] * self._num_rows) + coords[1]

    def get_tiles(self) -> list[Tile]:
        return self._tiles

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

    def draw(self, surface: pygame.Surface) -> None:
        for tile in self._tiles:
            tile.draw(surface)

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

    def get_tile_neighbors(self, tile: Tile) -> None:
        row_index, col_index = tile._coords
        if row_index - 1 >= 0:
            # top
            coords = (row_index - 1, col_index)
            tile_index = self.get_tile_index(coords)
            self._tiles[tile_index].activate_cell()
        if row_index + 1 < self._num_rows:
            # bottom
            coords = (row_index + 1, col_index)
            tile_index = self.get_tile_index(coords)
            self._tiles[tile_index].activate_cell()
        if col_index + 1 < self._num_cols:
            # right
            coords = (row_index, col_index + 1)
            tile_index = self.get_tile_index(coords)
            self._tiles[tile_index].activate_cell()
        if col_index - 1 > 0:
            # left
            coords = (row_index, col_index - 1)
            tile_index = self.get_tile_index(coords)
            self._tiles[tile_index].activate_cell()

    def activate_cell(self, selection: Selection):
        selection_coords = selection.get_coords(self.get_size())
        tile = self._tiles[self.get_tile_index(selection_coords)]
        tile.activate_cell()
        self.get_tile_neighbors(tile)

    def toggle_flag_mark(self, selection: Selection):
        selection_coords = selection.get_coords(self.get_size())
        self._tiles[self.get_tile_index(selection_coords)].toggle_flag_mark()

    def get_tile_index(self, coords: tuple[int, int]) -> int:
        row_index, col_index = coords
        tile_index = (row_index * self._num_cols) + col_index
        return tile_index

    def get_tiles(self) -> list[Tile]:
        return self._tiles

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

    def draw(self, surface: pygame.Surface) -> None:
        for tile in self._tiles:
            tile.draw(surface)

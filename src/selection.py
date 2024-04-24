import pygame

from constants import GRID_NUM_COLS, GRID_NUM_ROWS, TILE_SIZE
from tile import Tile


class Selection:
    def __init__(self) -> None:
        self._row_index = 0
        self._col_index = 0
        self._screen_pos = (0, 0)
        self._update_screen_pos()

    def go_left(self) -> None:
        self._col_index -= 1
        self._update_screen_pos()

    def go_right(self) -> None:
        self._col_index += 1
        self._update_screen_pos()

    def go_up(self) -> None:
        self._row_index -= 1
        self._update_screen_pos()

    def go_down(self) -> None:
        self._row_index += 1
        self._update_screen_pos()

    def get_coords(self, grid_size: tuple[int, int]) -> tuple[int, int]:
        return (self._row_index % grid_size[0], self._col_index % grid_size[1])

    def _update_screen_pos(self) -> None:
        self._screen_pos = self._get_screen_pos()

    def _get_screen_pos(self) -> tuple[float, float]:
        coords = (self._row_index, self._col_index)
        tile = Tile(coords)
        screen_pos = tile.get_screen_pos()
        return (screen_pos[0] + TILE_SIZE / 2, screen_pos[1] + TILE_SIZE / 2)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "green",
            self._screen_pos,
            5,
        )

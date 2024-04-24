import pygame

from constants import TILE_SIZE
from tile import get_tile_pos


class Selection:
    def __init__(self) -> None:
        self._row_i = 0
        self._col_i = 0
        self._pos = (0, 0)
        self._update_coords()

    def go_left(self) -> None:
        self._col_i -= 1
        self._update_coords()

    def go_right(self) -> None:
        self._col_i += 1
        self._update_coords()

    def go_up(self) -> None:
        self._row_i -= 1
        self._update_coords()

    def go_down(self) -> None:
        self._row_i += 1
        self._update_coords()

    def _update_coords(self) -> None:
        self._pos = self._get_screen_pos()

    def _get_screen_pos(self) -> tuple[float, float]:
        pos = get_tile_pos(self._row_i, self._col_i)
        return (pos[0] + TILE_SIZE / 2, pos[1] + TILE_SIZE / 2)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "red",
            self._pos,
            5,
        )

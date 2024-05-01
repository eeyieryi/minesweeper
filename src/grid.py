import random

import pygame

from cell import Cell, CellState
from selection import Selection


class Grid:
    def __init__(self, size: tuple[int, int], mines_num: int = 10) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._cells = self.initialize_cells()
        self._mines = self.plant_mines(mines_num)

    def initialize_cells(self) -> list[Cell]:
        cells: list[Cell] = []
        row_index, col_index = 0, 0
        for _ in range(self._num_rows * self._num_cols):
            coords = (row_index, col_index)
            cell = Cell(coords)
            cells.append(cell)
            if col_index + 1 == self._num_cols:
                row_index += 1  # down one row
                col_index = 0  # reset column
            else:
                col_index += 1  # go to the next column
        return cells

    def plant_mines(self, mines_num) -> None:
        choices: list[Cell] = []
        while len(choices) < mines_num:
            choice = random.choice(self._cells)
            if choice not in choices:
                choices.append(choice)
        return choices

    def get_cell_neighbors(self, cell: Cell) -> None:
        row_index, col_index = cell._coords
        if row_index - 1 >= 0:
            # top
            coords = (row_index - 1, col_index)
            cell_index = self.get_cell_index(coords)
            self._cells[cell_index].trigger()
        if row_index + 1 < self._num_rows:
            # bottom
            coords = (row_index + 1, col_index)
            cell_index = self.get_cell_index(coords)
            self._cells[cell_index].trigger()
        if col_index + 1 < self._num_cols:
            # right
            coords = (row_index, col_index + 1)
            cell_index = self.get_cell_index(coords)
            self._cells[cell_index].trigger()
        if col_index - 1 > 0:
            # left
            coords = (row_index, col_index - 1)
            cell_index = self.get_cell_index(coords)
            self._cells[cell_index].trigger()

    def trigger_cell(self, at_coords: tuple[int, int]):
        cell = self._cells[self.get_cell_index(at_coords)]
        if cell in self._mines:
            print("Game Over")
            cell.trigger()
            return False
        cell.trigger()
        return True
        # self.get_cell_neighbors(cell)

    def toggle_flag(self, at_coords: tuple[int, int]):
        self._cells[self.get_cell_index(at_coords)].toggle_flag_mark()

    def get_cell_index(self, coords: tuple[int, int]) -> int:
        row_index, col_index = coords
        cell_index = (row_index * self._num_cols) + col_index
        return cell_index

    def get_cells(self) -> list[Cell]:
        return self._cells

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

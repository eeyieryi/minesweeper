import random
from enum import Enum

from cell import Cell

GridState = Enum("GridState", ["CONTINUE", "SOLVED", "GAMEOVER"])


class Grid:
    def __init__(self, size: tuple[int, int], num_mines: int = 10) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._num_mines = num_mines
        self._state = GridState.CONTINUE
        self._setup()

    def _setup(self) -> None:
        self._cells = self._initialize_cells()
        self._mines = self._plant_mines(self._num_mines)
        self._label_cells()

    def _initialize_cells(self) -> list[Cell]:
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

    def _plant_mines(self, mines_num) -> list[Cell]:
        mine_cells: list[Cell] = []
        while len(mine_cells) < mines_num:
            choice = random.choice(self._cells)
            if choice not in mine_cells:
                mine_cells.append(choice)
        return mine_cells

    def _label_cells(self) -> None:
        for cell in self._cells:
            neighbors = self._get_cell_neighbors(cell)
            mine_count = 0
            for neighbor in neighbors:
                if neighbor in self._mines:
                    mine_count += 1
            cell.set_label(f"{mine_count}")

    def _get_cell_neighbors(self, cell: Cell) -> list[Cell]:
        row_index, col_index = cell._coords
        neighbors = []
        i = row_index - 1  # top
        j = col_index - 1  # left
        while i <= row_index + 1:
            while j <= col_index + 1:
                if i >= 0 and j >= 0 and i < self._num_rows and j < self._num_cols:
                    coords = (i, j)
                    cell_index = self._get_cell_index(coords)
                    neighbors.append(self._cells[cell_index])
                j += 1  # go right one col
            i += 1  # go down one row
            j = col_index - 1  # reset col to left most
        return neighbors

    def _get_cell_index(self, coords: tuple[int, int]) -> int:
        row_index, col_index = coords
        cell_index = (row_index * self._num_cols) + col_index
        return cell_index

    def get_state(self) -> GridState:
        return self._state

    def trigger_cell(self, at_coords: tuple[int, int]) -> None:
        cell = self._cells[self._get_cell_index(at_coords)]
        if cell in self._mines:
            self._state = GridState.GAMEOVER
        cell.trigger()

    def toggle_flag(self, at_coords: tuple[int, int]) -> None:
        cell_index = self._get_cell_index(at_coords)
        self._cells[cell_index].toggle_flag_mark()

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

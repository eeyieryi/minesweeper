import random
from enum import Enum

from config import Config
from game.cell import Cell, CellState

GridState = Enum("GridState", ["CONTINUE", "SOLVED", "GAMEOVER"])


class Grid:
    def __init__(self, cfg: Config) -> None:
        self._num_rows = cfg.grid_num_rows
        self._num_cols = cfg.grid_num_cols
        self._num_mines = cfg.grid_num_mines
        self._setup()

    def _setup(self) -> None:
        self._state = GridState.CONTINUE
        self._cell_count = self._num_rows * self._num_cols
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

    def _plant_mines(self, num_mines: int) -> list[Cell]:
        mine_cells: list[Cell] = []
        while len(mine_cells) < num_mines:
            choice = random.choice(self._cells)
            if choice not in mine_cells:
                mine_cells.append(choice)
        return mine_cells

    def _label_cells(self) -> None:
        for cell in self._cells:
            if cell in self._mines:
                cell.set_label("M")
            else:
                cell.set_label(f"{self._get_neighbors_mine_count(cell)}")

    def _get_neighbors_mine_count(self, cell: Cell) -> int:
        neighbors = self._get_cell_neighbors(cell)
        mine_count = 0
        for neighbor in neighbors:
            if neighbor in self._mines:
                mine_count += 1
        return mine_count

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

    def toggle_flag_at(self, coords: tuple[int, int]) -> None:
        if self.get_state() != GridState.CONTINUE:
            return
        cell_index = self._get_cell_index(coords)
        self._cells[cell_index].toggle_flag_mark()

    def trigger_cell_at(self, coords: tuple[int, int]) -> GridState:
        if self.get_state() != GridState.CONTINUE:
            return
        cell = self._cells[self._get_cell_index(coords)]
        cell_state = cell.get_state()
        if cell_state == CellState.FLAGGED:
            if cell in self._mines:
                cell.change_state_to(CellState.UNOPENED)
                cell.trigger()
                self._state = GridState.GAMEOVER
        elif cell_state == CellState.UNOPENED:
            cell.trigger()
            if cell.get_label() == "0":
                neighbors = self._get_cell_neighbors(cell)
                for neighbor in neighbors:
                    if neighbor.get_label() != "M":
                        self.trigger_cell_at(neighbor.get_coords())
            self._check_state()
        return self.get_state()

    def get_mines_left_count(self) -> int:
        return self._num_mines - len(self._get_flagged_cells())

    def _get_flagged_cells(self) -> list[Cell]:
        return list(
            filter(lambda cell: cell.get_state() == CellState.FLAGGED, self._cells)
        )

    def _get_opened_cells(self) -> list[Cell]:
        return list(
            filter(lambda cell: cell.get_state() == CellState.OPENED, self._cells)
        )

    def _check_state(self) -> None:
        if len(self._get_opened_cells()) == self._cell_count - self._num_mines:
            self._state = GridState.SOLVED

    def get_state(self) -> GridState:
        return self._state

    def get_cells(self) -> list[Cell]:
        return self._cells

    def get_mines(self) -> list[Cell]:
        return self._mines

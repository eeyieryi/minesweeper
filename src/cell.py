from enum import Enum

CellState = Enum("TileState", ["UNOPENED", "OPENED", "FLAGGED"])


class Cell:
    def __init__(
        self, coords: tuple[int, int], state: CellState = CellState.UNOPENED
    ) -> None:
        self._coords = coords
        self._state = state

    def get_coords(self) -> tuple[int, int]:
        return self._coords

    def get_state(self) -> CellState:
        return self._state

    def change_state_to(self, state: CellState) -> None:
        self._state = state

    def trigger(self) -> None:
        cell_state = self.get_cell_state()
        if cell_state == CellState.UNOPENED:
            self.change_state_to(CellState.OPENED)

    def toggle_flag_mark(self) -> None:
        cell_state = self.get_cell_state()
        if cell_state == CellState.UNOPENED:
            self.change_state_to(CellState.FLAGGED)
        elif cell_state == CellState.FLAGGED:
            self.change_state_to(CellState.UNOPENED)

    def get_cell_state(self) -> CellState:
        return self.get_state()

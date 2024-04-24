from enum import Enum

CellState = Enum("CellState", ["UNOPENED", "OPENED", "FLAGGED"])


class Cell:
    def __init__(self, state: CellState = CellState.UNOPENED) -> None:
        self._state = state

    def get_state(self) -> CellState:
        return self._state

    def change_state_to(self, state: CellState) -> None:
        self._state = state

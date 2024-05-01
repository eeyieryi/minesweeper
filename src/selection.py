class Selection:
    def __init__(self) -> None:
        self._row_index = 0
        self._col_index = 0

    def go_left(self) -> None:
        self._col_index -= 1

    def go_right(self) -> None:
        self._col_index += 1

    def go_up(self) -> None:
        self._row_index -= 1

    def go_down(self) -> None:
        self._row_index += 1

    def get_coords(self, grid_size: tuple[int, int]) -> tuple[int, int]:
        return (self._row_index % grid_size[0], self._col_index % grid_size[1])

from config import Config


class Selection:
    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg
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

    def get_coords(self) -> tuple[int, int]:
        return (
            self._row_index % self._cfg.grid_num_rows,
            self._col_index % self._cfg.grid_num_cols,
        )

    def reset(self) -> None:
        self._row_index = 0
        self._col_index = 0

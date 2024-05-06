from config import Config
from selection import Selection


class Utils:
    def __init__(self, cfg: Config, selection: Selection) -> None:
        self._cfg = cfg
        self._selection = selection

    def get_cell_screen_pos(self, coords: tuple[int, int]) -> tuple[float, float]:
        row_index = coords[0] % self._cfg.grid_num_rows
        col_index = coords[1] % self._cfg.grid_num_cols

        return (
            self._cfg.grid_margin_left + col_index * self._cfg.grid_cell_size,
            self._cfg.grid_margin_top + row_index * self._cfg.grid_cell_size,
        )

    def get_selection_screen_pos(self) -> tuple[float, float]:
        cell_coords = self.get_cell_screen_pos(self._selection.get_coords())
        return (
            cell_coords[0] + self._cfg.grid_cell_size / 2,
            cell_coords[1] + self._cfg.grid_cell_size / 2,
        )

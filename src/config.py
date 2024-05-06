from enum import Enum

EDifficulty = Enum("Difficulty", ["beginner", "intermediate", "expert"])


class Difficulty:
    def __init__(
        self, grid_num_rows, grid_num_cols, grid_num_mines, grid_cell_size
    ) -> None:
        self.grid_num_rows = grid_num_rows
        self.grid_num_cols = grid_num_cols
        self.grid_num_mines = grid_num_mines
        self.grid_cell_size = grid_cell_size


difficulties = {
    EDifficulty.beginner: Difficulty(
        grid_num_rows=9,
        grid_num_cols=9,
        grid_num_mines=10,
        grid_cell_size=25,
    ),
    EDifficulty.intermediate: Difficulty(
        grid_num_rows=16,
        grid_num_cols=16,
        grid_num_mines=40,
        grid_cell_size=25,
    ),
    EDifficulty.expert: Difficulty(
        grid_num_rows=16,
        grid_num_cols=30,
        grid_num_mines=99,
        grid_cell_size=20,
    ),
}


class Config:
    def __init__(self) -> None:
        self.window_title = "Minesweeper"
        self.window_width = 640
        self.window_height = 480
        self.change_difficulty_to(EDifficulty.beginner)

    def change_difficulty_to(self, difficulty: EDifficulty) -> None:
        self._difficulty = difficulties[difficulty]
        self.grid_num_rows = self._difficulty.grid_num_rows
        self.grid_num_cols = self._difficulty.grid_num_cols
        self.grid_cell_size = self._difficulty.grid_cell_size
        self.grid_num_mines = self._difficulty.grid_num_mines
        self.grid_margin_left = (
            self.window_width - (self.grid_num_cols * self.grid_cell_size)
        ) / 2
        self.grid_margin_top = (
            self.window_height - (self.grid_num_rows * self.grid_cell_size)
        ) / 2

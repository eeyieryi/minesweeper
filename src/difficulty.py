from enum import Enum

EDifficulty = Enum("Difficulty", ["beginner", "intermediate", "expert"])


class Difficulty:
    def __init__(
        self,
        grid_num_rows: int,
        grid_num_cols: int,
        grid_num_mines: int,
        grid_cell_size: int,
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

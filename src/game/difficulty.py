from enum import Enum

EDifficulty = Enum("Difficulty", ["beginner", "intermediate", "expert"])


class Difficulty:
    def __init__(
        self,
        edifficulty: EDifficulty,
        grid_num_rows: int,
        grid_num_cols: int,
        grid_num_mines: int,
    ) -> None:
        self.name = edifficulty.name
        self.grid_num_rows = grid_num_rows
        self.grid_num_cols = grid_num_cols
        self.grid_num_mines = grid_num_mines


difficulties = {
    EDifficulty.beginner: Difficulty(
        edifficulty=EDifficulty.beginner,
        grid_num_rows=9,
        grid_num_cols=9,
        grid_num_mines=10,
    ),
    EDifficulty.intermediate: Difficulty(
        edifficulty=EDifficulty.intermediate,
        grid_num_rows=16,
        grid_num_cols=16,
        grid_num_mines=40,
    ),
    EDifficulty.expert: Difficulty(
        edifficulty=EDifficulty.expert,
        grid_num_rows=16,
        grid_num_cols=30,
        grid_num_mines=99,
    ),
}

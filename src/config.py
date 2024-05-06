import pygame

from difficulty import EDifficulty, difficulties


class Config:
    def __init__(self) -> None:
        self.window_title = "Minesweeper"
        self.window_width = 640
        self.window_height = 480
        self.change_difficulty_to(EDifficulty.beginner)
        self.font = pygame.font.SysFont("monospace", 26)

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

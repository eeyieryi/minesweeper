from enum import Enum

import pygame

CellState = Enum("CellState", ["UNOPENED", "OPENED", "FLAGGED"])


class Tile:
    def __init__(self, state: CellState = CellState.UNOPENED) -> None:
        self._state = state

    def get_state(self) -> CellState:
        return self._state

    def change_state_to(self, state: CellState) -> None:
        self._state = state

    def __repr__(self) -> str:
        return f"Tile(CellState.{self._state.name})"


class Grid:
    def __init__(self, size: tuple[int, int]) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._tiles = self.make_tiles()

    def make_tiles(self) -> list[Tile]:
        tiles: list[Tile] = []
        for _ in range(self._num_rows * self._num_cols):
            tile = Tile()
            tiles.append(tile)
        return tiles

    def get_tiles(self) -> list[Tile]:
        return self._tiles

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

    def __repr__(self) -> str:
        return f"Grid({self._num_rows}, {self._num_cols})"


def draw_grid(screen: pygame.Surface, grid: Grid) -> None:
    grid_rows, grid_cols = grid.get_size()
    grid_tiles = grid.get_tiles()
    i, j = 0, 0
    for tile in grid_tiles:
        cell_state = tile.get_state()
        row_index = i % grid_rows
        col_index = j % grid_cols
        pos = (100 + row_index * 20, 100 + col_index * 20)
        if cell_state == CellState.UNOPENED:
            pygame.draw.circle(screen, "black", pos, 5)
        elif cell_state == CellState.FLAGGED:
            pygame.draw.circle(screen, "red", pos, 5)
        elif cell_state == CellState.OPENED:
            pygame.draw.circle(screen, "white", pos, 5)
        if i + 1 == grid_rows:
            i = 0
            j += 1
        else:
            i += 1


def run():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    grid_size = (9, 9)
    grid = Grid(size=grid_size)

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # draw to screen
        screen.fill("gray")
        draw_grid(screen, grid)
        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)
        # running = False


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

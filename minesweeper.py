from enum import Enum

import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
GRID_NUM_COLS = 9
GRID_NUM_ROWS = 9
GRID_SIZE = (GRID_NUM_COLS, GRID_NUM_ROWS)
TILE_SIZE = 25
GRID_MARGIN_LEFT = (WINDOW_WIDTH - (GRID_NUM_COLS * TILE_SIZE)) / 2
GRID_MARGIN_TOP = (WINDOW_HEIGHT - (GRID_NUM_ROWS * TILE_SIZE)) / 2


CellState = Enum("CellState", ["UNOPENED", "OPENED", "FLAGGED"])


class Cell:
    def __init__(self, state: CellState = CellState.UNOPENED) -> None:
        self._state = state

    def get_state(self) -> CellState:
        return self._state

    def change_state_to(self, state: CellState) -> None:
        self._state = state

    def __repr__(self) -> str:
        return f"Cell(state=CellState.{self._state.name})"


class Tile:
    def __init__(self, pos: tuple[float, float]) -> None:
        self._pos = pos
        self._cell = Cell()

    def get_cell_state(self) -> CellState:
        return self._cell.get_state()

    def draw(self, surface: pygame.Surface):
        cell_state = self._cell.get_state()
        if cell_state == CellState.UNOPENED:
            pygame.draw.rect(
                surface,
                "grey",
                pygame.Rect(self._pos[0], self._pos[1], TILE_SIZE - 1, TILE_SIZE - 1),
            )
        elif cell_state == CellState.FLAGGED:
            pygame.draw.circle(surface, "red", self._pos, 5)
        elif cell_state == CellState.OPENED:
            pygame.draw.circle(surface, "white", self._pos, 5)
        pass

    def __repr__(self) -> str:
        return f"Tile(pos=({self._pos[0]}, {self._pos[1]}))"


def get_tile_pos(row_i: int, column_i: int) -> tuple[float, float]:
    row_index = row_i % GRID_NUM_ROWS
    col_index = column_i % GRID_NUM_COLS
    tile_pos = (
        GRID_MARGIN_LEFT + col_index * TILE_SIZE,
        GRID_MARGIN_TOP + row_index * TILE_SIZE,
    )
    return tile_pos


class Grid:
    def __init__(self, size: tuple[int, int]) -> None:
        self._num_rows = size[0]
        self._num_cols = size[1]
        self._tiles = self.make_empty_grid_tiles()

    def make_empty_grid_tiles(self) -> list[Tile]:
        tiles: list[Tile] = []
        row_i, col_i = 0, 0
        for _ in range(self._num_rows * self._num_cols):
            tile = Tile(pos=get_tile_pos(row_i, col_i))
            tiles.append(tile)
            if col_i + 1 == GRID_NUM_COLS:
                row_i += 1  # down one row
                col_i = 0  # reset column
            else:
                col_i += 1  # go to the next column
        return tiles

    def get_tiles(self) -> list[Tile]:
        return self._tiles

    def get_size(self) -> tuple[int, int]:
        return (self._num_rows, self._num_cols)

    def draw(self, surface: pygame.Surface) -> None:
        for tile in self._tiles:
            tile.draw(surface)

    def __repr__(self) -> str:
        return f"Grid(size=({self._num_rows}, {self._num_cols}))"


def run():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    running = True

    grid = Grid(size=GRID_SIZE)

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # draw to screen
        screen.fill("black")
        grid.draw(screen)
        pygame.display.flip()

        # limit FPS to 60
        clock.tick(60)
        # running = False


if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()

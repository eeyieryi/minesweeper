from enum import Enum

import pygame

from config import Config
from game.grid import Grid
from game_state import GameState
from selection import Selection
from ui.ui import Ui


class Minesweeper:
    def __init__(self, config: Config) -> None:
        self._cfg = config
        self._state = GameState.PLAYING
        self._setup()

    def _setup(self) -> None:
        self._selection = Selection(self._cfg)
        self._ui = Ui(
            self._cfg, self._selection
        )  # TODO: remember to reset selection when resetting grid
        self._grid = Grid(self._cfg)  # TODO: move from here
        self._running = True

    def get_state(self) -> GameState:
        return self._state

    def change_state_to(self, state: GameState) -> None:
        self._state = state

    def handle_keydown_events(self, key: int) -> None:
        game_state = self.get_state()
        if key == pygame.K_q:
            self.kill()
        if game_state == GameState.PLAYING:
            if key == pygame.K_h:
                self._selection.go_left()
            elif key == pygame.K_l:
                self._selection.go_right()
            elif key == pygame.K_k:
                self._selection.go_up()
            elif key == pygame.K_j:
                self._selection.go_down()
            elif key == pygame.K_SPACE:
                self._grid.toggle_flag_at(self._selection.get_coords())
            elif key == pygame.K_RETURN:
                self._grid.trigger_cell_at(self._selection.get_coords())

    def handle_mousedown_event(self, event) -> None:
        # handle pygame.MOUSEBUTTONDOWN
        game_state = self.get_state()
        if game_state == GameState.PLAYING:
            coords = self._ui.get_coords_from_screen_pos(event.pos)
            if coords:
                if event.button == 1:
                    # left click
                    self._grid.trigger_cell_at(coords)
                elif event.button == 3:
                    # right click
                    self._grid.toggle_flag_at(coords)

    def draw(self, surface) -> None:
        game_state = self.get_state()
        self._ui.draw(surface, game_state, self._grid)

    def is_running(self) -> bool:
        return self._running

    def kill(self) -> None:
        self._running = False

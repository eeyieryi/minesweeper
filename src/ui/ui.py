from typing import Literal

import pygame

from config import Config
from game.cell import CellState
from game.difficulty import EDifficulty
from game.grid import Grid
from game_state import GameState
from selection import Selection
from ui.fonts import FontSize, font_filepath


class Ui:
    def __init__(self, cfg: Config, selection: Selection) -> None:
        self._cfg = cfg
        self._selection = selection
        self._current_menu_selection = 0
        self._setup_fonts()
        self._setup_ui_surfaces()
        self._show_selection = False

    def activate_selection(self) -> None:
        self._show_selection = True

    def _setup_fonts(self) -> None:
        self._fonts = {
            FontSize.Small: pygame.Font(font_filepath, 26),
            FontSize.Medium: pygame.Font(font_filepath, 30),
            FontSize.Large: pygame.Font(font_filepath, 72),
            FontSize.XLarge: pygame.Font(font_filepath, 96),
        }

    def _setup_ui_surfaces(self) -> None:
        self.game_title_text = self._fonts[FontSize.XLarge].render(
            self._cfg.window_title.upper(), True, "blue"
        )
        self._play_button_text = self._fonts[FontSize.Large].render(
            "PLAY", True, "white"
        )
        self._exit_button_text = self._fonts[FontSize.Large].render(
            "EXIT", True, "white"
        )
        self._difficulty_settings_texts = {
            EDifficulty.beginner: self._fonts[FontSize.Large].render(
                EDifficulty.beginner.name.upper(), True, "green"
            ),
            EDifficulty.intermediate: self._fonts[FontSize.Large].render(
                EDifficulty.intermediate.name.upper(), True, "yellow"
            ),
            EDifficulty.expert: self._fonts[FontSize.Large].render(
                EDifficulty.expert.name.upper(), True, "red"
            ),
        }
        self._setup_ui_surfaces_positions()

    def _setup_ui_surfaces_positions(self) -> None:
        half_width = self._cfg.window_width / 2
        half_height = self._cfg.window_height / 2
        max_menu_item_width = self._difficulty_settings_texts[
            EDifficulty.intermediate
        ].get_width()
        self._difficulty_setting_start_y = half_height
        self._play_button_start_x = half_width - (
            self._play_button_text.get_width() / 2
        )
        self._play_button_start_y = half_height + 72
        self._exit_button_start_x = half_width - (
            self._exit_button_text.get_width() / 2
        )
        self._exit_button_start_y = half_height + 72 + 72
        self._outline_selection_start_x = half_width - max_menu_item_width / 2 - 10
        self._outline_selection_width = max_menu_item_width + 20
        self._outline_selection_height = 72 + 10
        self._update_outline_selection_y()

    def _update_outline_selection_y(self) -> None:
        half_height = self._cfg.window_height / 2
        self._outline_selection_start_y = (half_height - 10) + (
            72 * (self._current_menu_selection + 1)
        )

    def handle_mousedown_events(
        self, event
    ) -> Literal["PLAY"] | Literal["EXIT"] | None:
        mx, my = event.pos
        start_x = self._outline_selection_start_x - 20
        end_x = self._outline_selection_start_x + self._outline_selection_width + 20
        if mx >= start_x and mx <= end_x:
            rect_height = self._difficulty_settings_texts[
                EDifficulty.intermediate
            ].get_height()
            if (
                my >= self._difficulty_setting_start_y
                and my <= self._difficulty_setting_start_y + rect_height
            ):
                if mx < end_x - ((end_x - start_x) / 2):
                    self.select_menu_go_left()
                else:
                    self.select_menu_go_right()
            elif (
                my >= self._play_button_start_y
                and my <= self._play_button_start_y + rect_height
            ):
                # start game
                if self._current_menu_selection != 0:
                    self._current_menu_selection = 0
                    self._update_outline_selection_y()
                return self.get_current_menu_selection()
            elif (
                my >= self._exit_button_start_y
                and my <= self._exit_button_start_y + rect_height
            ):
                # exit game
                if self._current_menu_selection != 1:
                    self._current_menu_selection = 1
                    self._update_outline_selection_y()
                return self.get_current_menu_selection()

    def handle_mousemotion_events(self, event) -> None:
        self._show_selection = False
        mx, my = event.pos
        start_x = self._outline_selection_start_x - 20
        end_x = self._outline_selection_start_x + self._outline_selection_width + 20
        if mx >= start_x and mx <= end_x:
            rect_height = self._difficulty_settings_texts[
                EDifficulty.intermediate
            ].get_height()
            if (
                my >= self._play_button_start_y
                and my <= self._play_button_start_y + rect_height
            ):
                if self._current_menu_selection != 0:
                    self._current_menu_selection = 0
                    self._update_outline_selection_y()
            elif (
                my >= self._exit_button_start_y
                and my <= self._exit_button_start_y + rect_height
            ):
                if self._current_menu_selection != 1:
                    self._current_menu_selection = 1
                    self._update_outline_selection_y()

    def get_current_menu_selection(self) -> Literal["PLAY"] | Literal["EXIT"]:
        if self._current_menu_selection == 0:
            return "PLAY"
        elif self._current_menu_selection == 1:
            return "EXIT"
        raise Exception("Should never reach here")

    def select_menu_go_down(self) -> None:
        self._current_menu_selection += 1
        self._current_menu_selection %= 2
        self._update_outline_selection_y()

    def select_menu_go_up(self) -> None:
        self._current_menu_selection -= 1
        self._current_menu_selection %= 2
        self._update_outline_selection_y()

    def select_menu_go_right(self) -> None:
        next_difficulty = EDifficulty[self._cfg.get_current_difficulty().name].value + 1
        next_difficulty %= 3
        self._cfg.change_difficulty_to(list(EDifficulty)[next_difficulty - 1])

    def select_menu_go_left(self) -> None:
        next_difficulty = EDifficulty[self._cfg.get_current_difficulty().name].value - 1
        next_difficulty %= 3
        self._cfg.change_difficulty_to(list(EDifficulty)[next_difficulty - 1])

    def draw(self, surface: pygame.Surface, game_state: GameState, grid: Grid) -> None:
        if game_state == GameState.MAIN:
            self._draw_main_menu(surface)
        elif game_state == GameState.PLAYING:
            self._draw_grid_status(surface, grid)
            self._draw_grid(surface, grid)
            self._draw_selection(surface)
        elif game_state == GameState.OVER:
            self._draw_grid_status(surface, grid)
            self._draw_grid(surface, grid)

    def _draw_grid_status(self, surface: pygame.Surface, grid: Grid) -> None:
        img = self._fonts[FontSize.Medium].render(
            grid.get_state().name, True, (255, 0, 0)
        )
        surface.blit(img, (20, 20))

    def _draw_grid(self, surface: pygame.Surface, grid: Grid) -> None:
        for cell in grid.get_cells():
            cell_state = cell.get_state()
            cell_label = cell.get_label()
            x, y = self._get_cell_screen_pos(cell.get_coords())
            if cell_state == CellState.UNOPENED:
                pygame.draw.rect(
                    surface,
                    "grey",
                    pygame.Rect(
                        x,
                        y,
                        self._cfg.grid_cell_size - 1,
                        self._cfg.grid_cell_size - 1,
                    ),
                )
            elif cell_state == CellState.FLAGGED:
                pygame.draw.rect(
                    surface,
                    "red",
                    pygame.Rect(
                        x + 3,
                        y + 3,
                        self._cfg.grid_cell_size - 6,
                        self._cfg.grid_cell_size - 6,
                    ),
                )
            elif cell_state == CellState.OPENED:
                if cell in grid.get_mines():
                    pygame.draw.circle(
                        surface,
                        "white",
                        (
                            x + self._cfg.grid_cell_size / 2,
                            y + self._cfg.grid_cell_size / 2,
                        ),
                        7,
                    )
                else:
                    img = self._fonts[FontSize.Medium].render(
                        cell_label, True, (255, 0, 0)
                    )
                    surface.blit(img, (x + 6, y))

    def _draw_selection(self, surface: pygame.Surface) -> None:
        if self._show_selection:
            pygame.draw.circle(
                surface,
                "green",
                self._get_selection_screen_pos(),
                5,
            )

    def _get_cell_screen_pos(self, coords: tuple[int, int]) -> tuple[float, float]:
        row_index = coords[0] % self._cfg.grid_num_rows
        col_index = coords[1] % self._cfg.grid_num_cols

        return (
            self._cfg.grid_margin_left + col_index * self._cfg.grid_cell_size,
            self._cfg.grid_margin_top + row_index * self._cfg.grid_cell_size,
        )

    def _get_selection_screen_pos(self) -> tuple[float, float]:
        cell_coords = self._get_cell_screen_pos(self._selection.get_coords())
        return (
            cell_coords[0] + self._cfg.grid_cell_size / 2,
            cell_coords[1] + self._cfg.grid_cell_size / 2,
        )

    def get_coords_from_screen_pos(
        self, pos: tuple[int, int]
    ) -> tuple[int, int] | None:
        pos_x, pos_y = pos

        start_x, start_y = self._get_cell_screen_pos((0, 0))
        end_x, end_y = self._get_cell_screen_pos(
            (self._cfg.grid_num_rows - 1, self._cfg.grid_num_cols - 1)
        )
        end_x += self._cfg.grid_cell_size
        end_y += self._cfg.grid_cell_size

        if pos_x >= start_x and pos_x <= end_x and pos_y >= start_y and pos_y <= end_y:
            row_index = (
                (pos_y - start_y) // self._cfg.grid_cell_size
            ) % self._cfg.grid_num_rows
            col_index = (
                (pos_x - start_x) // self._cfg.grid_cell_size
            ) % self._cfg.grid_num_cols
            return (int(row_index), int(col_index))

    def _draw_main_menu(self, surface: pygame.Surface) -> None:
        half_width = self._cfg.window_width / 2
        half_height = self._cfg.window_height / 2
        max_menu_item_width = self._difficulty_settings_texts[
            EDifficulty.intermediate
        ].get_width()

        surface.blit(
            self.game_title_text,
            (half_width - (self.game_title_text.get_width() / 2), 96),
        )

        difficulty_setting_text = self._difficulty_settings_texts[
            self._cfg.get_current_difficulty()
        ]
        surface.blit(
            difficulty_setting_text,
            (
                half_width - (difficulty_setting_text.get_width() / 2),
                self._difficulty_setting_start_y,
            ),
        )

        px = half_width - max_menu_item_width / 2 - 20
        py = half_height + 30
        pygame.draw.polygon(
            surface,
            (110, 110, 110),
            [(px - 5, py), (px + 5, py - 10), (px + 5, py + 10)],
            3,
        )
        px = px + max_menu_item_width + 30
        py = half_height + 30
        pygame.draw.polygon(
            surface,
            (110, 110, 110),
            [(px + 5, py), (px - 5, py - 10), (px - 5, py + 10)],
            3,
        )

        surface.blit(
            self._play_button_text,
            (self._play_button_start_x, self._play_button_start_y),
        )
        surface.blit(
            self._exit_button_text,
            (self._exit_button_start_x, self._exit_button_start_y),
        )

        pygame.draw.rect(
            surface,
            (55, 55, 55),
            (
                self._outline_selection_start_x,
                self._outline_selection_start_y,
                self._outline_selection_width,
                self._outline_selection_height,
            ),
            5,
        )
import logging

import pygame.font
from pygame import display
from pygame import draw
from pygame.time import Clock

from config.settings import ColorEnum, OFFSET, FPS, HEIGHT, WIDTH
from models.game import GameOfLive

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ContentGameOfLiveView:
    def __init__(self, model: GameOfLive, screen, active_cell_color: ColorEnum = ColorEnum.BLUE_V2.value,
                 inactive_cell_color: ColorEnum = ColorEnum.WHITE.value, offset: int = OFFSET):
        self._model = model
        self._screen = screen
        self._active_color = active_cell_color
        self._inactive_color = inactive_cell_color
        self._offset = offset

    def _draw_pause_window(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = font.render('Pause', False, (0, 0, 0))
        surface = pygame.Surface(text_surface.get_size())
        surface.fill(ColorEnum.GREEN.value)
        surface.blit(text_surface, (0, 0))
        self._screen.blit(surface, (HEIGHT / 2, WIDTH / 2))

    def _draw_cells(self):
        for row in range(self._model.rows):
            for col in range(self._model._columns):
                y_scaled = row * self._model.scale
                x_scaled = col * self._model.scale
                color = self._inactive_color

                if self._model.board[row][col]:
                    color = self._active_color

                border = self._model.scale - self._offset
                draw.rect(self._screen, color, [x_scaled, y_scaled, border, border])

    def show(self):
        if self._model.is_paused:
            return self._draw_pause_window()

        self._draw_cells()


class MainWindow:

    def __init__(self, model: GameOfLive, screen, fps: int = FPS):
        self._model = model
        self._fps = fps
        self._screen = screen
        self._started: bool = False

    @property
    def screen(self):
        return self._screen

    def show(self):
        if not self._started:
            self._screen.fill(ColorEnum.BLACK.value)

            clock = Clock()
            clock.tick(self._fps)

            self._started = True

        content_window: ContentGameOfLiveView = ContentGameOfLiveView(self._model, self._screen)
        content_window.show()

    def run(self):
        self.show()
        display.update()

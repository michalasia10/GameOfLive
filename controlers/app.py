import pygame

from config.settings import *
from controlers.main_window_controler import MainWindowController
from models.buttons import Button
from models.game import GameOfLive
from view.game_view import MainWindow


class GameOfLiveApp:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(NAME)
        game_model = GameOfLive(WIDTH, HEIGHT, SCALER)

        pause_button = Button(pygame.K_SPACE)
        unpause_button = Button(pygame.K_RETURN)
        exit_button = Button(pygame.K_ESCAPE)

        screen = pygame.display.set_mode(SIZE)
        self._controller = MainWindowController(game_model, MainWindow(game_model, screen), pause_button, exit_button,
                                                unpause_button)

    def run(self):
        closed = False
        while not closed:
            self._controller.run()
            self._controller._model.run()
            self._controller._view.run()
            closed = self._controller._model.is_closed

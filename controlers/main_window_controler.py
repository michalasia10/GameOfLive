import logging
from time import sleep

import pygame
from pygame import event

from models.buttons import Button
from models.game import GameOfLive
from view.game_view import MainWindow

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MainWindowController:

    def __init__(self, model: GameOfLive = None, view: MainWindow = None, pause_button: Button = None,
                 exit_button: Button = None, unpause_button: Button = None):
        self._model = model
        self._view = view
        self._pause_button = pause_button
        self._exit_button = exit_button
        self._unpause_button = unpause_button

    def check_events(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                self._model.is_closed = True

            if e.type == pygame.KEYUP:

                if e.key == self._pause_button.key:
                    logger.info("Game is paused")
                    self._model.is_paused = True

                if e.key == self._exit_button.key:
                    self._model.is_closed = True
                    self._model.is_paused = True
                    logger.info("Game is exit")

                if e.key == self._unpause_button.key:
                    logger.info("Game is unpaused")
                    sleep(1)
                    self._model.is_paused = False

    def run(self):
        self.check_events()

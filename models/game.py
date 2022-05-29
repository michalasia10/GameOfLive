import logging

import numpy as np

from models.abstract import Game

logger = logging.getLogger(__name__)


class GameOfLive(Game):

    def __init__(self, width: int, height: int, scale: int):
        self._width = width
        self._height = height

        self._scale = scale

        self._columns = int(height / scale)
        self._rows = int(width / scale)

        self._shape = (self._rows, self._columns)
        self._board = np.random.randint(0, 2, self._shape)
        self._pause = False

    @property
    def scale(self):
        return self._scale

    @property
    def is_paused(self):
        return self._pause

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def board(self):
        return self._board

    @property
    def shape(self):
        return self._shape

    @staticmethod
    def get_neighbour(board, x, y, rows, columns):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + rows) % rows
                y_edge = (y + m + columns) % columns
                total += board[x_edge][y_edge]

        total -= board[x][y]
        return total

    def unpause(self):
        self._pause = False
        self.run()

    def pause(self):
        self._pause = True

    def run(self):

        if self._pause:
            logger.warning("Game is Paused")
            return

        next = np.ndarray(shape=(self._shape))

        for x in range(self._rows):
            for y in range(self._columns):
                state = self._board[x][y]
                neighbours = self.get_neighbour(self._board, x, y, self._rows, self._columns)

                if state == 0 and neighbours == 3:
                    next[x][y] = 1

                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0

                else:
                    next[x][y] = state

        self._board = next

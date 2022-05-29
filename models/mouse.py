from pygame import mouse


class Mouse:

    def __init__(self):
        self._position = mouse.get_pos()

    @property
    def position(self):
        return self._position
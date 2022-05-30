class Button:
    def __init__(self, key):
        self._key = key

    @property
    def key(self):
        return self._key

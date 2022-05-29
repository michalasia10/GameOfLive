from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def show(self):
        pass

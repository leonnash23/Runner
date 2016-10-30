from abc import ABCMeta, abstractmethod

from Abstract.Buttons import Buttons


class ButtonsListener(metaclass=ABCMeta):
    @abstractmethod
    def update(self, x, y, b: Buttons):
        pass

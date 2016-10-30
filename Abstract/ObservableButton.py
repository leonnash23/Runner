from abc import ABCMeta

from Abstract.Buttons import Buttons
from Abstract.ButtonsListener import ButtonsListener


class ObservableButton(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def register(self, observer: ButtonsListener):
        self.observers.append(observer)

    def notify_all(self, x, y, b: Buttons):
        for obs in self.observers:
            obs.update(x, y, b)

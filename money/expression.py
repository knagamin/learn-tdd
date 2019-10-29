from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):

    @abstractmethod
    def reduce(self, bank, to):
        pass

    @abstractmethod
    def plus(self, bank, to):
        pass

    @abstractmethod
    def times(self, multiplier):
        pass

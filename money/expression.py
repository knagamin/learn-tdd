from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):

    @abstractmethod
    def reduce(bank, to):
        pass

    @abstractmethod
    def plus(bank, to):
        pass

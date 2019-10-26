from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):

    @abstractmethod
    def reduce(to: str):
        pass

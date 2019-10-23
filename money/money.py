from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    _amount = 0

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._amount == other._amount
        return False

    def currency(self):
        return self._currency

    @abstractmethod
    def times(self):
        pass

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)


class Franc(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)

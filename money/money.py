class Money:
    _amount = 0

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self._currency == other._currency

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)


class Franc(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)

from money.expression import Expression


class Money(Expression):
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

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, to: str):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


class Sum(Expression):

    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


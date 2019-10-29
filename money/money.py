from money.expression import Expression


class Money(Expression):
    _amount = 0

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount and
                self._currency == other._currency)

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


class Sum(Expression):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = (self.augend.reduce(bank, to)._amount
                  + self.addend.reduce(bank, to)._amount)
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier),
                   self.addend.times(multiplier))


class Bank:

    rates = dict()

    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(self, from_c, to_c):
        if (from_c == to_c):
            return 1

        key = (from_c, to_c)
        return self.rates[key]

    def add_rate(self, from_c, to_c, rate):
        key = (from_c, to_c)
        self.rates[key] = rate

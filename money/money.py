class Money:
    _amount = 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._amount == other._amount

        return False

    def dollar(self, amount):
        return Dollar(amount)


class Dollar(Money):

    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

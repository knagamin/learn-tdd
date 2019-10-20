class Franc:

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__

        return False

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
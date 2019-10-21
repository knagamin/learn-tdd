class Money:
    _amount = 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._amount == other._amount

        return False
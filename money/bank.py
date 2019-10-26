from money.money import Money, Sum
from money.expression import Expression


class Bank:

    def reduce(self, source: Expression, to: str):
        sum = source
        return sum.reduce(to)

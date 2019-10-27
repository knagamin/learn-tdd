from money.money import Money, Sum
from money.expression import Expression


class Bank:

    rates = dict()

    def reduce(self, source: Expression, to: str):
        return source.reduce(self, to)

    def add_rate(self, cur_from: str, cur_to: str, rate: int ):
        pass

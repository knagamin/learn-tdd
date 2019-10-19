class Dollar():

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, dollar_obj):
        return self.amount == dollar_obj.amount

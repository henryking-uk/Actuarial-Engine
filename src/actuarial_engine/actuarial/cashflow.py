from finance.interest import Interest

class Cashflow:
    def __init__(self, time, amount, type):
        self.time: int = time
        self.amount: float = amount
        self.type: str = type

    def present_value(self, interest: Interest):
        return self.amount / (interest.rate + 1)**self.time
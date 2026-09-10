from actuarial_engine.finance.interest import Interest

class Cashflow:
    def __init__(self, time, amount, cashflow_type):
        self.time: int = time
        self.amount: float = amount
        self.cashflow_type: str = cashflow_type

    def present_value(self, interest: Interest):
        return self.amount * interest.discount_factor(self.time)
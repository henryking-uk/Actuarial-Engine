from actuarial_engine.mortality.mortality_table import MortalityTable

class Mortality:
    def __init__(self, table):
        self.table: MortalityTable = table

    def px(self, age, sex):
        """Probability of surviving the next year."""

        return 1 - self.table.qx(age, sex)

    def t_px(self, age, sex, t): 
        """Probability of surviving t years"""

        t_px = 1

        for k in range(t):
            t_px *= self.px(age + k, sex)
        
        return t_px

    def t_qx(self, age, sex, t): 
        """Probability of dying within t years"""

        return 1 - self.t_px(age, sex, t)

    def deferred_qx(self, age, sex, t): 
        """Probability of surviving t years and then dying in the following year"""

        return self.t_px(age, sex, t) * self.table.qx(age + t, sex)
    
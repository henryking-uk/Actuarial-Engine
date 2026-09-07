from mortality.mortality_table import MortalityTable

class Mortality:
    def __init__(self, table):
        self.table: MortalityTable = table

    def px(self, age, sex, year):
        """Probability of surviving the next year."""

        return 1 - self.table.qx(age, sex, year)

    def t_px(self, age, sex, year, t): 
        """Probability of surviving t years"""

        t_px = self.px(age, sex, year)

        for k in range(1, t):
            t_px *= self.px(age + k, sex, year)
        
        return t_px

    def t_qx(self, age, sex, year, t): 
        """Probability of dying within t years"""

        return 1 - self.t_px(age, sex, year, t)

    def deferred_qx(self, age, sex, year, t): 
        """Probability of surviving t years and then dying in the following year"""

        return self.t_px(age, sex, year, t) * self.table.qx(age + t, sex, year)
    
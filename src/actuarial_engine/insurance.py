from actuarial_engine.actuarial.actuarial_values import ActuarialValues

class Insurance:
    def __init__(self, actuarial_values, sum_assured, age, sex, year):
        self.actuarial_values: ActuarialValues = actuarial_values
        self.sum_assured = sum_assured
        self.age = age
        self.sex = sex
        self.year = year

    def benefit_t(self, t):
        return self.sum_assured

class WholeLifeAssurance(Insurance):
    def premium(self):
        A = self.actuarial_values.whole_life_assurance_factor(self.age, self.sex, self.year)
        a = self.actuarial_values.whole_life_annuity_due_factor(self.age, self.sex, self.year)
        premium = self.sum_assured * A / a
        return premium

class InflationLinkedWholeLife(Insurance):
    def __init__(self, actuarial_values, sum_assured, age, sex, year, inflation_rate):
        super().__init__(actuarial_values, sum_assured, age, sex, year)
        self.inflation_rate = inflation_rate

    def benefit_t(self, t):
        return (1 + self.inflation_rate)**t * self.sum_assured

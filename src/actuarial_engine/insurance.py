from actuarial_engine.actuarial.actuarial_values import ActuarialValues

class WholeLifeAssurance:
    def __init__(self, actuarial_values):
        self.actuarial_values = actuarial_values

    def premium(self, age, sex, year, sum_assured):
        A = self.actuarial_values.whole_life_assurance_factor(age, sex, year)
        a = self.actuarial_values.whole_life_annuity_due_factor(age, sex, year)



        premium = sum_assured * A / a

        return premium
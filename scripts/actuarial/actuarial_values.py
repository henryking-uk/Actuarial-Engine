from scripts.mortality.mortality import Mortality
from scripts.finance.interest import Interest

class ActuarialValues:
    def __init__(self, mortality, interest):
        self.mortality:Mortality = mortality
        self.interest:Interest = interest

    def whole_life_assurance_factor(self, age, sex, year):

        Ax = 0

        for t in range(1, 101 - age):
            t__px = self.mortality.t_px(age, sex, year, t-1)
            qxt__ = self.mortality.table.qx(age + t - 1, sex, year)
            vt = self.interest.discount_factor(t)

            Ax = Ax + t__px * qxt__ * vt

        return Ax 
        

    def whole_life_annuity_due_factor(self, age, sex, year):
        pass

    def term_assurance_factor(self, age, sex, year, t):
        pass
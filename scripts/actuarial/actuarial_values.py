from scripts.mortality.mortality import Mortality
from scripts.finance.interest import Interest

class ActuarialValues:
    def __init__(self, mortality, interest):
        self.mortality:Mortality = mortality
        self.interest:Interest = interest

    def whole_life_assurance_factor(self, age, sex, year):
        """Present value of a whole-life death benefit of £1."""

        Ax = 0

        for t in range(1, 101 - age):
            t__px = self.mortality.t_px(age, sex, year, t-1)
            qxt__ = self.mortality.table.qx(age + t - 1, sex, year)
            vt = self.interest.discount_factor(t)

            Ax = Ax + t__px * qxt__ * vt

        return Ax 
        

    def whole_life_annuity_due_factor(self, age, sex, year):
        """Present value of a whole-life annuity-due of £1 per year."""

        ax = 0

        for t in range(0, 101 - age):
            t_px = self.mortality.t_px(age, sex, year, t)
            vt = self.interest.discount_factor(t)
            ax = ax + t_px * vt

            print(f"Annuity , {age + t, t_px}")

        return ax

    def term_assurance_factor(self, age, sex, year, n):
        """Present value of a term assurance death benefit of £1."""

        Axn = 0

        for t in range(1, n+1):
            t__px = self.mortality.t_px(age, sex, year, t-1)
            qxt__ = self.mortality.table.qx(age + t - 1, sex, year)
            vt = self.interest.discount_factor(t)

            Axn = Axn + t__px * qxt__ * vt

            print(f"Assurnace, {age + t - 1, self.mortality.table.qx(age, sex, year)}")

        return Axn
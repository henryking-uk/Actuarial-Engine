from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest

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


        return ax

    def term_assurance_factor(self, age, sex, year, n):
        """Present value of a term assurance death benefit of £1."""

        Axn = 0

        for t in range(1, n+1):
            t__px = self.mortality.t_px(age, sex, year, t-1)
            qxt__ = self.mortality.table.qx(age + t - 1, sex, year)
            vt = self.interest.discount_factor(t)

            Axn = Axn + t__px * qxt__ * vt


        return Axn

    def temporary_annuity_due_factor(self, age, sex, year, n):
        """Present value of an n-year temporary annuity-due of 1."""
        axn = 0

        for t in range(n):
            t_px = self.mortality.t_px(age, sex, year, t)
            vt = self.interest.discount_factor(t)
            axn += t_px * vt

        return axn

    def term_assurance_premium(self, age, sex, year, n, sum_assured):
        """Annual level premium for an n-year term assurance."""
        Axn = self.term_assurance_factor(age, sex, year, n)
        axn = self.temporary_annuity_due_factor(age, sex, year, n)

        return sum_assured * Axn / axn

    def increasing_whole_life_assurance_factor(self, age, sex, year, g):
        """Present value factor for a whole-life death benefit increasing at rate g."""

        Ax_g = 0

        for t in range(1, 101 - age):
            t__px = self.mortality.t_px(age, sex, year, t-1)
            qxt__ = self.mortality.table.qx(age + t - 1, sex, year)
            vt = self.interest.discount_factor(t)
            growth_term = (1 + g)**(t - 1)

            Ax_g = Ax_g + t__px * qxt__ * vt * growth_term

        return Ax_g 
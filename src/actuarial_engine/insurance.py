from actuarial_engine.actuarial.actuarial_values import ActuarialValues
from actuarial_engine.client import Client

class Insurance:
    def __init__(self, actuarial_values, sum_assured, client):
        self.actuarial_values: ActuarialValues = actuarial_values
        self.sum_assured = sum_assured
        self.client: Client = client

    def benefit_t(self, t):
        return self.sum_assured

class WholeLifeAssurance(Insurance):
    def premium(self):
        A = self.actuarial_values.whole_life_assurance_factor(self.client.age, self.client.sex)
        a = self.actuarial_values.whole_life_annuity_due_factor(self.client.age, self.client.sex)
        premium = self.sum_assured * A / a
        return premium

class InflationLinkedWholeLife(Insurance):
    def __init__(self, actuarial_values, sum_assured, client, inflation_rate):
        super().__init__(actuarial_values, sum_assured, client)
        self.inflation_rate = inflation_rate

    def premium(self):
        Ax_g = self.actuarial_values.increasing_whole_life_assurance_factor(self.client.age, self.client.sex, self.inflation_rate)
        a = self.actuarial_values.whole_life_annuity_due_factor(self.client.age, self.client.sex)

        premium = self.sum_assured * Ax_g / a

        return premium

    def benefit_t(self, t):
        return (1 + self.inflation_rate)**t * self.sum_assured

class TermAssurance(Insurance):
    def __init__(self, actuarial_values, sum_assured, client, term_length):
        super().__init__(actuarial_values, sum_assured, client)
        self.term_length = term_length

    def benefit_t(self, t):
        if t >= self.term_length:
            return 0
        else:
            return self.sum_assured

    def premium(self):
        Axn = self.actuarial_values.term_assurance_factor(self.client.age, self.client.sex, self.term_length)
        axn = self.actuarial_values.temporary_annuity_due_factor(self.client.age, self.client.sex, self.term_length)

        premium = self.sum_assured * Axn / axn
        return premium


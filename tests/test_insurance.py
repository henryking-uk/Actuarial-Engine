import pytest

from actuarial_engine.insurance import WholeLifeAssurance, InflationLinkedWholeLife
from actuarial_engine.client import Client
from actuarial_engine.actuarial.actuarial_values import ActuarialValues
from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest

# ActuarialValues fixture

@pytest.fixture
def actuarial_values():
    table = MortalityTable("data/processed/mortality_data.csv", 2024)
    mortality = Mortality(table)
    interest = Interest(0.05)
    return ActuarialValues(mortality, interest)

# Client fixture

@pytest.fixture
def client():
    return Client(40, "Male")


# tests for WholeLifeAssurance

def test_WholeLifeAssurance_benefit_t(actuarial_values, client):
    policy = WholeLifeAssurance(actuarial_values, 100000, client)

    assert policy.sum_assured == policy.benefit_t(0)
    assert policy.sum_assured == policy.benefit_t(100)



# tests for InflationLinkedWholeLife

def test_InflationLinkedWholeLife_benefit_t(actuarial_values, client):
    rate = 0.03

    policy = InflationLinkedWholeLife(actuarial_values, 500000, client, rate)

    assert policy.benefit_t(5) == pytest.approx(500000*(1 + rate)**5)
import pytest

from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest
from actuarial_engine.actuarial.actuarial_values import ActuarialValues


@pytest.fixture
def actuarial_values():
    table = MortalityTable("data/processed/mortality_data.csv", 2024)
    mortality = Mortality(table)
    interest = Interest(0.05)

    return ActuarialValues(mortality, interest)


def test_whole_life_assurance_factor(actuarial_values):
    Ax = actuarial_values.whole_life_assurance_factor(
        88, "Male"
    )

    assert Ax == pytest.approx(0.7708997267505175)


def test_whole_life_annuity_due_factor(actuarial_values):
    ax = actuarial_values.whole_life_annuity_due_factor(
        88, "Male"
    )

    assert ax == pytest.approx(4.434862152887779)


def test_whole_life_assurance_factor_between_zero_and_one(actuarial_values):
    Ax = actuarial_values.whole_life_assurance_factor(
        88, "Male"
    )

    assert 0 < Ax < 1


def test_whole_life_annuity_due_is_positive(actuarial_values):
    ax = actuarial_values.whole_life_annuity_due_factor(
        88, "Male"
    )

    assert ax > 0
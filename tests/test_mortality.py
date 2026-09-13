import pytest

from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality


@pytest.fixture
def mortality():
    table = MortalityTable("data/processed/mortality_data.csv", 2024)
    return Mortality(table)


def test_px(mortality):
    qx = mortality.table.qx(88, "Male")

    assert mortality.px(88, "Male") == pytest.approx(1 - qx)


def test_zero_year_survival(mortality):
    assert mortality.t_px(88, "Male", 0) == 1


def test_one_year_survival(mortality):
    assert mortality.t_px(88, "Male", 1) == pytest.approx(
        mortality.px(88, "Male")
    )


def test_survival_recursion(mortality):
    lhs = mortality.t_px(88, "Male", 5)

    rhs = (
        mortality.t_px(88, "Male", 4)
        * mortality.px(92, "Male")
    )

    assert lhs == pytest.approx(rhs)


def test_t_qx(mortality):
    survival = mortality.t_px(88, "Male", 5)

    assert mortality.t_qx(88, "Male", 5) == pytest.approx(
        1 - survival
    )


def test_invalid_sex(mortality):
    with pytest.raises(ValueError):
        mortality.px(88, "Dog")


def test_invalid_age(mortality):
    with pytest.raises(ValueError):
        mortality.px(101, "Male")
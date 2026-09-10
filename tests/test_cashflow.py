import pytest

from actuarial_engine.finance.interest import Interest
from actuarial_engine.actuarial.cashflow import Cashflow


@pytest.fixture
def interest():
    rate = 0.05
    return Interest(rate)

@pytest.mark.parametrize(
    "time, amount, expected",
    [
        (0, 100, 100),
        (1, 100, 100 / 1.05),
        (10, 100, 100 / 1.05**10),
        (5, -500, -500 / 1.05**5),
    ]
)
def test_present_value(time, amount, expected, interest):
    cf = Cashflow(time, amount, "premium")

    assert cf.present_value(interest) == pytest.approx(expected)

def test_cashflow_attributes():
    cf = Cashflow(5, 250, "premium")

    assert cf.time == 5
    assert cf.amount == 250
    assert cf.cashflow_type == "premium"
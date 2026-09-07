import pytest

from scripts.finance.interest import Interest


@pytest.fixture
def interest():
    return Interest(0.05)


def test_discount_factor(interest):
    assert interest.discount_factor(10) == pytest.approx(
        1 / 1.05**10
    )


def test_accumulation_factor(interest):
    assert interest.accumulation_factor(10) == pytest.approx(
        1.05**10
    )


def test_discount_and_accumulation_are_inverses(interest):
    discount = interest.discount_factor(10)
    accumulation = interest.accumulation_factor(10)

    assert discount * accumulation == pytest.approx(1)


def test_discount_rate(interest):
    assert interest.discount_rate() == pytest.approx(
        0.05 / 1.05
    )
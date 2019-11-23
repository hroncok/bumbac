import pytest

def bumbac(num):
    if num % 15 == 0:
        return "bumbac"
    if num % 3 == 0:
        return "bum"
    if num % 5 == 0:
        return "bac"
    return str(num)


@pytest.mark.parametrize("n", [15])
def test_bumbac_threefives_are_bumbacs(n):
    assert bumbac(n) == "bumbac"
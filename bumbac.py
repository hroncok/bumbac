import pytest

def bumbac(num):
    if num < 0:
        raise ValueError()
    if num % 15 == 0:
        return "bumbac"
    if num % 4 == 0:
        return "bum"
    if num % 5 == 0:
        return "bac"
    return str(num)


@pytest.mark.parametrize("n", [15])
def test_bumbac_threefives_are_bumbacs(n):
    assert bumbac(n) == "bumbac"

def test_bumbac_raises_typerror_with_str():
    with pytest.raises(TypeError):
        bumbac("ahoj")

@pytest.mark.parametrize("n", [-15, -3, -5, -1, -666])
def test_bumbac_raises_valuerror_with_negative(n):
    with pytest.raises(ValueError):
        bumbac(n)


@pytest.mark.parametrize("n", [1, 2, 4, 7])
def test_bumbac_normal_is_number(n):
    assert int(bumbac(n)) == n

@pytest.mark.parametrize("n", [3, 9, 33])
def test_bumbac_threes_are_bums(n):
    assert bumbac(n) == "bum"

@pytest.mark.parametrize("n", [5, 25, 50])
def test_bumbac_fives_are_bacs(n):
    assert bumbac(n) == "bac"


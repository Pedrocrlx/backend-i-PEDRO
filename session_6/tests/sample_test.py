from pytest import raises
from src.session_6.sample import add, multiply, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(2, 2) == 4


def test_factorial():
    with raises(AssertionError, match="vai joreg mete num"):
        factorial(-1)
    assert factorial(6) == 720

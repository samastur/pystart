import pystart.module


def test_returns_five_does_not_return_four():
    assert pystart.module.returns_five() != 4


def test_returns_five_returns_five():
    assert pystart.module.returns_five() == 5

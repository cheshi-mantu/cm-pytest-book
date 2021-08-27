import pytest

def test_pass():
    pass

def test_fail():
    assert False

@pytest.mark.xfail()
def test_xpass():
    pass

@pytest.mark.xfail()
def test_xfail():
    assert False

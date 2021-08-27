import allure
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)

def test_failing_strings():
    assert "tra-tata" == "trata-ta"

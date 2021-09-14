import allure

@allure.suite("Second steps")
@allure.story("smoking pytest")
@allure.feature("tuple assertion")
@allure.title("Assert a tuple and test will fail")
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)

@allure.suite("Second steps")
@allure.story("smoking pytest and assertions")
@allure.feature("tuple assertion")
@allure.title("Assert a string and test will fail")
def test_failing_strings():
    assert "tra-tata" == "trata-ta"
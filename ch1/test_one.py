import allure

@allure.suite("First steps")
@allure.story("smoking pytest")
@allure.feature("various assertions")
@allure.title("Assert a tuple")
def test_passing():
    with allure.step("Assert 123 versus 123"):
        assert (1, 2, 3) == (1, 2, 3)

@allure.suite("First steps")
@allure.story("smoking pytest")
@allure.feature("strings assertions")
@allure.title("Assert two identical strings")
def test_almost_same_assertion():
    with allure.step("Assert tra-tata vs. tra-tata"):
        assert "tra-tata" == "tra-tata"

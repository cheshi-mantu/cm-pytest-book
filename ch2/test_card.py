import allure
from cards import Card
from allure import attachment_type

@allure.title("Testing an object for the class 'Card' with non-default values")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_field_access():
    with allure.step("Creating a class instance"):
        allure.attach("Card('something', 'brian', 'todo', 123)", name="Object created as", attachment_type=attachment_type.TEXT)
        c = Card("something", "brian", "todo", 123)
    with allure.step("Assert summary is 'something'"):
        assert c.summary == "something"
    with allure.step("Assert owner is 'brian'"):
        assert c.owner == "brian"
    with allure.step("Assert state is 'todo'"):
        assert c.state == "todo"
    with allure.step("Assert id is 123"):
        assert c.id == 123

@allure.title("Testing the default values of an object for the class 'Card'")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_defaults():
    with allure.step("Creating object as 'Card()'"):
        c = Card()
    with allure.step("Assert sumary is None"):
        assert c.summary is None
    with allure.step("Assert owner is None"):
        assert c.owner is None
    with allure.step("Assert state is todo"):
        assert c.state == "todo"
    with allure.step("Assert id is None"):
        assert c.id is None

@allure.title("Test equality of two objects of the class 'Card' created with the same parameters")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_equality():
    with allure.step("Creating object as 'Card()'"):
        c1 = Card("something", "brian", "todo", 123)
        allure.attach("c1 = Card('something', 'brian', 'todo', 123)", name="Object 'c1' created as", attachment_type=attachment_type.TEXT)
    with allure.step("Creating object as 'Card()'"):
        c2 = Card("something", "brian", "todo", 123)
        allure.attach("c2 = Card('something', 'brian', 'todo', 123)", name="Object 'c2' created as", attachment_type=attachment_type.TEXT)
    with allure.step("Assert object c1 == c2"):
        assert c1 == c2

@allure.title("Two object of the class 'Cards' with different IDs should be equal. ID to be ignored.")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_equality_with_diff_ids():
    with allure.step("Creating object c1"):
        c1 = Card("something", "brian", "todo", 123)
        allure.attach("c1 = Card('something', 'brian', 'todo', 123)", name="Object 'c1' created as", attachment_type=attachment_type.TEXT)
        with allure.step("Creating object c2"):
            c2 = Card("something", "brian", "todo", 4567)
            allure.attach("c2 = Card('something', 'brian', 'todo', 4567)", name="Object 'c2' created as", attachment_type=attachment_type.TEXT)
    assert c1 == c2

@allure.title("Two object of the class 'Cards' with different IDs should not be equal if params differ")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_inequality():
    with allure.step("Creating object c1"):
        c1 = Card("something", "brian", "todo", 123)
    with allure.step("Creating object c2"):
        c2 = Card("completely different", "okken", "done", 123)
    with allure.step("Assert c1 != c2"):
        assert c1 != c2

@allure.title("Two objects should be equal when c2 created from dictionary data")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_from_dict():
    with allure.step("Creating object c1"):
        c1 = Card("something", "brian", "todo", 123)
    with allure.step("Creating dictionary to create c2 from with the same params as c1"):
        c2_dict = {"summary": "something",
                   "owner": "brian",
                   "state": "todo",
                   "id": 123}
    with allure.step("Creating object c2 from the dictionary"):
        c2 = Card.from_dict(c2_dict)
    with allure.step("Asserting c1 == c2"):
        assert c1 == c2

@allure.title("Two dictionaries should be equal when dictionary c2 created from c1 object")
@allure.feature("Pytest book by Okken")
@allure.story("Chapter 2")
def test_to_dict():
    with allure.step("Creating object c1"):
        c1 = Card("something", "brian", "todo", 123)
    with allure.step("Save c1.to_dict to c2"):
        c2 = c1.to_dict()
    with allure.step("Create c2_expected dictionary to compare with c2"):
        c2_expected = {"summary": "something",
               "owner": "brian",
               "state": "todo",
               "id": 123}
    with allure.step("Comparing c2 with c2_expected dictionary"):
        assert c2 == c2_expected

import pytest
import cards

def test_no_path_raises():
    with pytest.raises(TypeError):
        c = cards.CardsDB()


def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex) as excinfo:
        c = cards.CardsDB()

def test_raises_with_info2():
    with pytest.raises(TypeError) as excinfo:
        c = cards.CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(excinfo.value)

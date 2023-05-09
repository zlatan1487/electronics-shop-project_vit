from src.keyboard import KeyBoard
import pytest

# TestCase#1 check method __str__ for class KeyBoard[Item]
kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_value_keyboard():
    assert str(kb) == "Dark Project KD87A"


# TestCase#2 check property language for class KeyBoard[MixinLanguage]
def test_property_language():
    assert str(kb.language) == "EN"


# TestCase#3 change property language for class KeyBoard[MixinLanguage]
def test_change_property_language():
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"

    with pytest.raises(AttributeError):
        kb.language = "CH"


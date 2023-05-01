from src.phone import Phone
from src.item import Item


# TestCase#1 check method __repr__, __str__ class Phone
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_value_phone():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


item1 = Item("Смартфон", 10000, 20)


# TestCase#2 check method __add__ class Item and class Phone
def test_value_item():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    try:
        phone1.number_of_sim = 0
        assert False, "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
    except ValueError:
        assert True


"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_class_item1():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.pay_rate == 1.0
    assert item1.calculate_total_price() == 200000
    item1.pay_rate = 0.8
    assert item1.pay_rate == 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


item2 = Item("Ноутбук", 20000, 5)


def test_class_item2():
    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5
    assert item2.pay_rate == 1.0
    assert item2.calculate_total_price() == 100000
    item2.pay_rate = 0.8
    assert item2.pay_rate == 0.8
    assert item2.price == 20000


def test_long_name():
    item3 = Item('смартфон', 10000, 5)
    try:
        item3.name = "СуперСмартфон"
        assert False, "ValueError: Длина наименования товара не может быть больше 10 символов"
    except ValueError:
        assert True


def test_string_to_number():
    assert Item.string_to_number("10.0") == 10
    assert Item.string_to_number("5") == 5


def test_name_getter():
    item = Item("Смартфон", 10.0, 5)
    assert item.name == "Смартфон"
    Item.instantiate_from_csv()
    item_ = Item.all[0]
    assert item_.name == "Смартфон"


def test_length_all():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


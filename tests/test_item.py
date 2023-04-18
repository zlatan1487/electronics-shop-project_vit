"""Здесь надо написать тесты с использованием pytest для модуля item."""
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


def test_get_all():
    print(Item.all)
    assert Item.all == [item1, item2]

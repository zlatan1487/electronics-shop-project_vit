"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
path = "src/items.csv"


item1 = Item("Смартфон", 10000, 20)


# TestCase#1 item1
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


# TestCase#2 item2
def test_class_item2():
    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5
    assert item2.pay_rate == 1.0
    assert item2.calculate_total_price() == 100000
    item2.pay_rate = 0.8
    assert item2.pay_rate == 0.8
    assert item2.price == 20000


# TestCase#3 check long name

def test_long_name():
    item3 = Item('смартфон', 10000, 5)
    try:
        item3.name = "СуперСмартфон"
        assert False, "ValueError: Длина наименования товара не может быть больше 10 символов"
    except ValueError:
        assert True


# TestCase#4 check string_to_number

def test_string_to_number():
    assert Item.string_to_number("10.0") == 10
    assert Item.string_to_number("5") == 5


# TestCase#5 check test_name_getter

def test_name_getter():
    item = Item("Смартфон", 10.0, 5)
    assert item.name == "Смартфон"
    Item.instantiate_from_csv(path)
    item_ = Item.all[0]
    assert item_.name == "Смартфон"


# TestCase#6 check length array

def test_length_all():
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5


# TestCase#7 check method representation
def test_method_representation():
    repr_ = Item("Телефон", 18000, 10)
    assert repr(repr_) == "Item('Телефон', 18000, 10)"


# TestCase#8 check method string
def test_method_string():
    string_ = Item("Yottanewton", 15000, 13)
    assert str(string_) == 'Yottanewton'


# TestCase#9 check case FileNotFoundError
def test_instantiate_from_csv_fake_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('fake.csv')


# TestCase#10 check case for corrupted file
def test_instantiate_from_csv_error_file(tmp_path):
    filepath = tmp_path / "corrupted_items.csv"
    with open(filepath, "w") as file:
        file.write("name,price,quantity\n")
        file.write("hello 100,10,15\n")
        file.write("world 25,3\n")  # Invalid 'quantity' value

    with pytest.raises(TypeError):
        Item.instantiate_from_csv(filepath)

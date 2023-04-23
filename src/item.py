import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        filepath = "../src/items.csv"
        if not os.path.exists(filepath):
            filepath = "src/items.csv"

        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                cls.all.append(cls(line['name'], int(line['price']), int(line['quantity'])))

        return cls.all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Длина наименования товара не может быть больше 10 символов")

    @staticmethod
    def string_to_number(number):
        return int(float(number))



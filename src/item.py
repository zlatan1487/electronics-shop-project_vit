import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, message):
        self.message = message
    #     self.message = "Файл item.csv поврежден"


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
        super().__init__()

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

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name ,self.price, self.quantity}'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, filepath):
        cls.all.clear()
        try:
            with open(filepath, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))
        except ValueError:
            raise ValueError(f"Отсутствует значение в колонке")
        except KeyError:
            raise InstantiateCSVError("Файл items.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

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



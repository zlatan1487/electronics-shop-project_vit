from src.item import Item
import os.path

filepath = os.path.join("../src/", "items.csv")
if __name__ == '__main__':

    print(filepath)
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(filepath)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(filepath)
    # InstantiateCSVError: Файл item.csv поврежден

from src.item import Item


class MixinLanguage:
    __slots__ = ['EN', 'RU', 'UA']

    _language = 'EN'

    def change_lang(self):
        MixinLanguage._language = self.__slots__[1]
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


kb = KeyBoard('Dark Project KD87A', 9600, 5)






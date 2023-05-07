from src.item import Item


class MixinLanguage:
    __slots__ = ['EN', 'RU']

    _language = 'EN'

    def change_lang(self):
        current_index = self.__slots__.index(self._language)
        next_index = (current_index + 1) % len(self.__slots__)
        MixinLanguage._language = self.__slots__[next_index]
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








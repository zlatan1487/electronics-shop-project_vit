from src.item import Item


class MixinLanguage:
    _languages = ["RU", "EN"]

    def __init__(self):
        self._language = "EN"

    def change_lang(self):

        current_index = self._languages.index(self._language)
        next_index = (current_index + 1) % len(self._languages)
        self._language = self._languages[next_index]
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


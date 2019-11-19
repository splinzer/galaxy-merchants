import roman
from types import MappingProxyType
class Question():

    def __init__(self):
        self._answer_types = MappingProxyType({
            "HOW_MUCH":"",
            "HOW_MANY":"",
            "NO_IDEA":"I have no idea what you are talking about"
        })
        self._symbol = roman.Roman()

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if not isinstance(symbol, roman.Roman.__bases__):
            raise TypeError
        self._symbol = symbol

    def process_question(self):
        pass
import roman


class Question():
    def __init__(self):
        self._answers = {
            "HOW_MUCH":
            "%s is %d",
            "HOW_MANY":
            "%s is %d Credits",
            "NO_IDEA":
            "I have no idea what you're talking about"
        }
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

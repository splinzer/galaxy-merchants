import re
from types import MappingProxyType
from exceptions import InvalidSymbolException, InvalidSyntaxException


class Roman():
    def __init__(self):
        self._valid_symbols = MappingProxyType({
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        })
        self._validator = "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    @property
    def valid_symbols(self):
        return self._valid_symbols

    @property
    def validator(self):
        return self._validator

    def roman_to_arabic(self, roman):
        total = 0
        local_max = 0
        if not self._validate_roman(roman):
            raise InvalidSyntaxException()

        for i in reversed(roman):
            r = self._get_value_by_symbol(i)
            if local_max <= r:
                total += r
                local_max = r
            else:
                total -= r
        return total

    def _validate_roman(self, roman):
        if not isinstance(roman, str):
            raise TypeError
        if not re.match(self._validator, roman):
            return False
        return True

    def _get_value_by_symbol(self, symbol):
        try:
            return self._valid_symbols[symbol]
        except:
            raise InvalidSymbolException(symbol)


if __name__ == "__main__":

    r = Roman()
    print(r.valid_symbols)
    print(r.roman_to_arabic('MCMIII'))

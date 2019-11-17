#! /usr/bin/env python
class RomanSymbols():
    def __init__(self):
        self._valid_symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    @property
    def valid_symbols(self):
        return self._valid_symbols

    def get_value_by_name(self, symbol):
        if not isinstance(symbol, str):
            raise TypeError
        return self._valid_symbols[symbol.upper()]

    def check_symbols_validation(self, symbol):
        if not symbol or symbol not in self._valid_symbols.keys():
            return False
        return True


if __name__ == "__main__":
    pass

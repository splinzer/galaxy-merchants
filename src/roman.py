#!/usr/bin/env python
# pylint: disable=C0303
import re
from types import MappingProxyType
from exception import InvalidSymbolException, InvalidSyntaxException


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
        """(dict): return valid Roman symbols
        """
        return self._valid_symbols

    @property
    def validator(self):
        """(str): return the validate syntax for Roman symbol
        """
        return self._validator

    def roman_to_arabic(self, roman: str) -> int:
        """The function is to translate roman into arabic numbers

            Args:
                roman(str): Roman statements

            Returns:
                total(int): Arabit number

            Raises:
                InvalidSyntaxException

        """
        total = 0
        previous = 0
        if not self.__validate_roman(roman):
            raise InvalidSyntaxException()

        for i in reversed(roman):
            current = self.get_value_by_symbol(i)
            if previous <= current:
                total += current
                previous = current
            else:
                total -= current
        return total

    def get_value_by_symbol(self, symbol: str) -> int:
        """Get the arabic value for it's roman symbol

            Args:
                symbol(str): Roman symbol

            Returns:
                (int): corresponding arabic number

            Raises:
                InvalidSymbolException

        """
        try:
            return self._valid_symbols[symbol]
        except:
            raise InvalidSymbolException(symbol)

    def __validate_roman(self, roman: str) -> bool:
        """
            Validate if roman statement exists syntax error

            Args:
                symbol(str): Roman symbol

            Returns:
                (bool): The return value. True for NO syntax error

        """
        if not re.match(self._validator, roman):
            return False
        return True

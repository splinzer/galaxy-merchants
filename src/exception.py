#! /usr/bin/env python
class InvalidSymbolException(Exception):
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return f"{self.symbol} is invalid symbol."


class InvalidSyntaxException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f"Invalid Roman Syntax"


class ConflictSymbolValueException(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f"the value of {self.key} conflicts existed one"
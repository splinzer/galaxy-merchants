#! /usr/bin/env python
class InvalidSymbolException(Exception):
    def __init__(self, symbol):
        self.symbol = symbol
    
    def __str__(self):
        return f'{self.symbol} is invalid symbol.'


class InvalidSyntaxException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Invalid Syntax'


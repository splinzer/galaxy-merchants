#! /usr/bin/env python

class RuleViolationException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'RuleViolationException: {self.message}'


class UnknownSymbolException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'UnknownSymbolException: {self.message}'


from types import MappingProxyType
import re
import roman


class Command():
    def __init__(self):
        self._symbol = roman.Roman()
        self._command_types = MappingProxyType({
            "ASSIGMENT":
            "^([A-Za-z]+) is ([I|V|X|L|C|D|M])$",
            "CREDITS":
            "^([A-Za-z]+)([A-Za-z\\s]*) is ([0-9]+) ([c|C]redits)$",
            "HOW_MUCH":
            "^[h|H]ow much is (([A-Za-z\\s])+)\\?$",
            "HOW_MANY":
            "^[h|H]ow many [c|C]redits is (([A-Za-z\\s])+)\\?$",
        })

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if not isinstance(symbol, roman.Roman.__bases__):
            raise TypeError
        self._symbol = symbol

    def process_command(self, line):

        if re.match(self._command_types("ASSIGMENT"), line):
            pass

        elif re.match(self._command_types("CREDITS"), line):
            pass

        elif re.match(self._command_types("HOW_MUCH"), line):
            pass

        elif re.match(self._command_types("HOW_MANY"), line):
            pass

        else:
            pass

    def _process_assignment(self, line):
        pass

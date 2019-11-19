from types import MappingProxyType
import re
import roman


class Command():
    def __init__(self):
        self.__cmds = {}
        self._symbol = roman.Roman()
        self._command_types = MappingProxyType({
            "ASSIGMENT":
            "^([A-Za-z]+) is ([A-Z])$",
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
            self.__process_assignment(line)

        elif re.match(self._command_types("CREDITS"), line):
            self.__process_credits(line)

        elif re.match(self._command_types("HOW_MUCH"), line):
            pass

        elif re.match(self._command_types("HOW_MANY"), line):
            pass

        else:
            pass

    def __process_assignment(self, line):
        pass

    def __process_credits(self, line):
        pass

    def __process_how_much(self, line):
        pass

    def __process_how_many(self, line):
        pass

    def __process_no_idea(self, line):
        pass
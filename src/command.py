#!/usr/bin/env python
from types import MappingProxyType
import re
import roman

from exception import ConflictSymbolValueException


class Command():
    def __init__(self):
        self.__intergalactic = {}
        self.__metal = {}
        self._symbol = roman.Roman()
        self._command_types = MappingProxyType({
            "ASSIGMENT":
            "^([A-Za-z]+) is ([A-Z])$",
            "CREDITS":
            "^([A-Za-z]+)([A-Za-z\\s]*) is ([0-9]+) (Credits)$",
            "HOW_MUCH":
            "^how much is (([A-Za-z\\s])+)\\?$",
            "HOW_MANY":
            "^how many Credits is (([A-Za-z\\s])+)\\?$",
        })

    @property
    def symbol(self):
        """(obj): Setup the symbol, example: Roman

            Raises:
                TypeError
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if not isinstance(symbol, roman.Roman.__bases__):
            raise TypeError
        self._symbol = symbol

    def process_command(self, line: str):
        """ Process each line and catagorize for further processing

            Args:
                line(str): each line of test input

            Returns:
                None: 
                (str):
             
        """
        if re.match(self._command_types["ASSIGMENT"], line):
            return self.__process_assignment(line)

        elif re.match(self._command_types["CREDITS"], line):
            return self.__process_credits(line)

        elif re.match(self._command_types["HOW_MUCH"], line):
            return self.__process_how_much(line)

        elif re.match(self._command_types["HOW_MANY"], line):
            return self.__process_how_many(line)

        else:
            return self.__process_no_idea()

    def __process_assignment(self, line):
        """ Process command line matches ASSIGNMENT regex

            Args:
                line(str): line of test input matches ASSIGNMENT regex

            Returns:
                None

        """
        line = line.strip("\n").replace(" is ", "|").split("|")
        intergalactic, roman = line[0], line[-1]

        self.__intergalactic[intergalactic] = roman

    def __process_credits(self, line):
        """ Process command line matches CREDITS regex

            Args:
                line(str): line of test input matches CREDITS regex

            Returns:
                None

        """
        line = line.strip(" Credits\n").replace(" is ", "|").split("|")
        intergalactic_metal, credit = line[0], int(line[-1])

        roman = ''
        # avoid variable name like 'i' or 'j', use meaningful word like 'word'
        # it will make you code more readable 
        for i in intergalactic_metal.split(" "):
            if i in self.__intergalactic.keys():
                roman += self.__intergalactic[i]
            else:
                metal = i
        self.__metal[metal] = credit / self._symbol.roman_to_arabic(roman)

    def __process_how_many(self, line):
        """ Process command line matches HOW_MANY regex

            Args:
                line(str): line of test input matches HOW_MANY regex

            Returns:
                (str): eg: glob glob Sliver is XXXX Credits

        """
        line = line.replace("how many Credits is ", "").strip(" ?\n")
        intergalactic_metal = line

        roman = ''
        for i in intergalactic_metal.split(" "):
            if i in self.__intergalactic.keys():
                roman += self.__intergalactic[i]
            else:
                metal = i

        decimal = int(
            self._symbol.roman_to_arabic(roman) * self.__metal[metal])

        return f"{intergalactic_metal} is {decimal} Credits"

    def __process_how_much(self, line):
        """ Process command line matches HOW_MUCH regex

            Args:
                line(str): line of test input matches HOW_MUCH regex

            Returns:
                (str): eg: glob glob is XXXX

        """
        line = line.replace("how much is ", "").strip(" ?\n")
        intergalactic = line

        roman = ''
        for i in line.split(" "):
            roman += self.__intergalactic[i]

        decimal = self._symbol.roman_to_arabic(roman)
        return f"{intergalactic} is {decimal}"

    def __process_no_idea(self):
        return "I have no idea what you are talking about"

#! /usr/bin/env python
import command


class Paragraph():
    def __init__(self):
        self.__answer = []
        self._cmd = command.Command()

    @property
    def cmd(self):
        """(obj): Setup the parsing command

            Raises:
                TypeError
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        if not isinstance(cmd, command.Command.__bases__):
            raise TypeError
        self._cmd = cmd

    def read(self, filename: str) -> None:
        """ Read the Test input file into self.__answer

            Args:
                filename(str): Test input file name

            Returns:
                None

            Raise:
                FileNotExistedError                
        """
        with open(filename) as f:
            for line in f:
                if self._cmd.process_command(line):
                    self.__answer.append(self._cmd.process_command(line))

    def output(self) -> None:
        for i in self.__answer:
            print(i)
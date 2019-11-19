#!/usr/bin/env python
# pylint: disable=C0103
from command import Command
from question import Question


class Paragraph():
    def __init__(self):
        self.__cache = {}
        self.__answer = []
        self._cmd = Command()
        self._question = Question()

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        if not isinstance(cmd, object):
            raise TypeError
        self._cmd = cmd

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, question):
        if not isinstance(question, object):
            raise TypeError
        self._question = question

    def read(self, intput_filename):
        with open(intput_filename) as f:
            for line in f:
                if "?" in line:
                    pass
                else:
                    symbol, value = self.cmd.process_command(line)
                    self.__cache[symbol] = value

    def output(self):
        with open('output_file.txt', "w") as f:
            for i in self.__answer:
                f.write(i + '\n')

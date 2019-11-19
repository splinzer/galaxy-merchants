#!/usr/bin/env python
# pylint: disable=C0103
import command
import question


class Paragraph():

    QUESTION_MARK = '?'

    def __init__(self):
        self.__cache = {}
        self.__answer = []
        self._cmd = command.Command()
        self._question = question.Question()

    @property
    def cmd(self):
        return self._cmd

    @property
    def question(self):
        return self._question

    @cmd.setter
    def cmd(self, cmd):
        if not isinstance(cmd, command.Command.__bases__):
            raise TypeError
        self._cmd = cmd

    @question.setter
    def question(self, question):
        if not isinstance(question, question.Question.__bases__):
            raise TypeError
        self._question = question

    def read(self, filename):
        with open(filename) as f:
            for line in f:
                pass

    def output(self):
        with open("output_file.txt", "w") as f:
            for i in self.__answer:
                f.write(i + '\n')

#! /usr/bin/env python
import command


class Paragraph():
    def __init__(self):
        self.__answer = []
        self._cmd = command.Command()

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        if not isinstance(cmd, command.Command.__bases__):
            raise TypeError
        self._cmd = cmd

    def read(self, filename):
        with open(filename) as f:
            for line in f:
                if self._cmd.process_command(line):
                    self.__answer.append(self._cmd.process_command(line))

    # def output(self):
    #     with open("../output_file.txt", "w") as f:
    #         for i in self.__answer:
    #             f.write(i + '\n')

    def output(self):
        print("Test Output:\n")
        for i in self.__answer:
            print(i)
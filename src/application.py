#!/usr/bin/env python
# pylint: disable=R0903, C0103
from paragraph import Paragraph

def main(filename):
    paragraph = Paragraph()
    paragraph.read(filename)
    paragraph.output()

if __name__ == "__main__":

    input_filename = '../input_file.txt'
    main(input_filename)
    
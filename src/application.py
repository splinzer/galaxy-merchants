#!/usr/bin/env python
# pylint:disable=C0103
import paragraph

def main(filename):
    pgph = paragraph.Paragraph()
    pgph.read(filename)
    pgph.output()

if __name__ == "__main__":

    input_filename = '../input_file.txt'
    main(input_filename)
    
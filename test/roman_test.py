import unittest
from Src.src.roman import Roman
from Src.src.exception import InvalidSyntaxException

class TestRoman(unittest.TestCase):

    def test_get_value_by_symbol(self):
        roman = Roman()
        self.assertEqual(roman._valid_symbols["I"],1)
        self.assertEqual(roman._valid_symbols["V"],5)
        self.assertEqual(roman._valid_symbols["X"],10)
        self.assertEqual(roman._valid_symbols["L"],50)
        self.assertEqual(roman._valid_symbols["C"],100)
        self.assertEqual(roman._valid_symbols["D"],500)
        self.assertEqual(roman._valid_symbols["M"],1000)

    def test_roman_to_arabic(self):
        roman = Roman()
        self.assertEqual(roman.roman_to_arabic('II'),2)
        self.assertEqual(roman.roman_to_arabic('MCMIII'),1903)
        with self.assertRaises(InvalidSyntaxException):
            roman.roman_to_arabic("DDD")


if __name__ == '__main__':
    unittest.main()
import unittest
from roman import Roman
from exception import InvalidSyntaxException


class TestRoman(unittest.TestCase):
    def setUp(self):
        self.roman = Roman()

    def tearDown(self):
        pass

    def test_get_value_by_symbol(self):
        self.assertEqual(self.roman.get_value_by_symbol("I"), 1)
        self.assertEqual(self.roman.get_value_by_symbol("V"), 5)
        self.assertEqual(self.roman.get_value_by_symbol("X"), 10)
        self.assertEqual(self.roman.get_value_by_symbol("L"), 50)
        self.assertEqual(self.roman.get_value_by_symbol("C"), 100)
        self.assertEqual(self.roman.get_value_by_symbol("D"), 500)
        self.assertEqual(self.roman.get_value_by_symbol("M"), 1000)

    def test_roman_to_arabic(self):
        self.assertEqual(self.roman.roman_to_arabic('II'), 2)
        self.assertEqual(self.roman.roman_to_arabic('MCMIII'), 1903)
        with self.assertRaises(InvalidSyntaxException):
            self.roman.roman_to_arabic("IIII")


if __name__ == '__main__':
    unittest.main()

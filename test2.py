import unittest
from main2 import romano_a_decimal

class TestRomanToDecimal(unittest.TestCase):
    def test_1(self):
        decimal = romano_a_decimal('I')
        self.assertEqual(decimal, 1)
    def test_18(self):
        decimal = romano_a_decimal('XVIII')
        self.assertEqual(decimal, 18)
    def test_24(self):
        decimal = romano_a_decimal('XXIV')
        self.assertEqual(decimal, 24)
    def test_52(self):
        decimal = romano_a_decimal('LII')
        self.assertEqual(decimal, 52)
    def test_104(self):
        decimal = romano_a_decimal('CIV')
        self.assertEqual(decimal, 104)
    def test_232(self):
        decimal = romano_a_decimal('CCXXXII')
        self.assertEqual(decimal, 232)
    def test_2045(self):
        decimal = romano_a_decimal('MMXLV')
        self.assertEqual(decimal, 2045)
    def test_3006(self):
        decimal = romano_a_decimal('MMMVI')
        self.assertEqual(decimal, 3006)

if __name__ == '__main__':
    unittest.main()
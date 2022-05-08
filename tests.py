import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition_a(self):
        nums = [1,2,3,4,5]
        self.assertEqual(15, Calculator().add(*nums))

    def test_addition_b(self):
        self.assertEqual(360, Calculator().add(180+180))

    def test_multiply(self):
        self.assertEqual(45, Calculator().multiply(9,5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
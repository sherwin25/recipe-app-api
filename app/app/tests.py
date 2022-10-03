

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5,6)

        self.assertEqual(res,11)

    
    def test_subtract_numbers(self):
        """Test subtracting numbers"""

        res = calc.subtract(10,15)

        self.assertEqual(res,5)

    
    def test_multiplying_numbers(self):
        """Test multiplying numbers"""
        res = calc.multiply(3, 5)

        self.assertEqual(res, 15)

        
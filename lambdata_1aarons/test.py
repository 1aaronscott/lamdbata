import unittest
import complex


class Complex_Test(unittest.TestCase):
    """ Test that complex number subtraction works.
    number1 = 5+4i
    number2 = 12+2i
    result = -7+2i
    """

    def test_subtract(self):
        number1 = complex.Complex(5, 4)
        number2 = complex.Complex(12, 2)
        self.assertTrue(complex.Complex(-7, 2), number1+number2)


if __name__ == '__main__':
    unittest.main()

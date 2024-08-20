import unittest

from mymodule import square, double
class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)

    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3), 6)
        self.assertEqual(double(4), 8)


if __name__ == '__main__':
    unittest.main()
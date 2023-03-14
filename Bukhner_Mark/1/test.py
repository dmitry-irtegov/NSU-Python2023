import unittest

from main import cumulative_sum


class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        self.assertEqual([0], cumulative_sum([]))

    def test_simple(self):
        self.assertEqual([0, 1, 3, 6], cumulative_sum([1, 2, 3]))

    def test_negative(self):
        self.assertEqual([0, -1, -3, -6], cumulative_sum([-1, -2, -3]))

    def test_float(self):
        self.assertEqual([0.0, 0.0, 0.3, 1000.8], cumulative_sum([0.0, 0.3, 1000.5]))

    def test_large(self):
        number = 10 ** 100
        count = 10 ** 5
        lst = [number] * count
        expected = [0]
        for x in lst:
            expected.append(expected[-1] + x)
        self.assertEqual(expected, cumulative_sum(lst))

if __name__ == '__main__':
    unittest.main()

import unittest
from app import largest_continuous


class TestContinuousSum(unittest.TestCase):

    def setup(self):
        pass

    def test_sum_array_positive_numbers(self):
        self.assertEqual(largest_continuous([5, 1, 2, 6]), 14)
        self.assertEqual(largest_continuous([3, 1, 8, 4]), 16)

    def test_sum_array_all_negative_numbers(self):
        self.assertEqual(largest_continuous([-1, -4, -5, -7]), -1)
        self.assertEqual(largest_continuous([-9, -2, -6, -3]), -2)

    def test_sum_array_all_integers(self):
        self.assertEqual(largest_continuous([6, -4, 9, 1, 2, -3]), 14)
        self.assertEqual(largest_continuous([1, -3, 7, 1, -1, 5]), 12)

    def test_sum_array_zeroes(self):
        self.assertEqual(largest_continuous([0, 0]), 0)
        self.assertEqual(largest_continuous([0, 0, 0, 0]), 0)

    def test_sum_array_one_element(self):
        self.assertEqual(largest_continuous([1]), 1)
        self.assertEqual(largest_continuous([-4]), -4)


if __name__ == '__main__':
    unittest.main()

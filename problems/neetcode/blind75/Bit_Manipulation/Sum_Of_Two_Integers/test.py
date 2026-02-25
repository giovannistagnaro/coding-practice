import unittest
from solution import Solution

class TestSumOfTwoIntegers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sum_of_two_integers_example1(self):
        a, b = 1, 1
        expected_result = 2
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

    def test_sum_of_two_integers_example2(self):
        a, b = 4, 7
        expected_result = 11
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

    def test_sum_of_two_integers_zero(self):
        a, b = 0, 0
        expected_result = 0
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

    def test_sum_of_two_integers_one_negative(self):
        a, b = -5, 4
        expected_result = -1
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

    def test_sum_of_two_integers_one_negative_positive(self):
        a, b = -4, 5
        expected_result = 1
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

    def test_sum_of_two_integers_two_negatives(self):
        a, b = -4, -7
        expected_result = -11
        result = self.solution.getSum(a, b)
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
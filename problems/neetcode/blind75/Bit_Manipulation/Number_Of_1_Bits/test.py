import unittest
from solution import Solution

class TestNumberOf1Bits(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_number_of_1_bits_example1(self):
        input = 23
        expected_result = 4
        result = self.solution.hammingWeight(input)

        self.assertEqual(expected_result, result)

    def test_number_of_1_bits_example2(self):
        input = 2147483645
        expected_result = 30
        result = self.solution.hammingWeight(input)

        self.assertEqual(expected_result, result)

    def test_number_of_1_bits_zero(self):
        input = 0
        expected_result = 0
        result = self.solution.hammingWeight(input)

        self.assertEqual(expected_result, result)

    def test_number_of_1_bits_max_int(self):
        input = 4294967295
        expected_result = 32
        result = self.solution.hammingWeight(input)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
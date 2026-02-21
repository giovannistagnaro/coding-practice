import unittest
from solution import Solution

class TestCountingBits(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_counting_bits_example1(self):
        input = 4
        expected_result = [0,1,1,2,1]
        result = self.solution.countBits(input)

        self.assertEqual(expected_result, result)

    def test_counting_bits_zero(self):
        input = 0
        expected_result = [0]
        result = self.solution.countBits(input)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
import unittest
from solution import Solution

class TestReverseBits(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverse_bits_example1(self):
        n = 21
        expected_result = 2818572288
        result = self.solution.reverseBits(n)
        self.assertEqual(expected_result, result)

    def test_reverse_bits_zero(self):
        n = 0
        expected_result = 0
        result = self.solution.reverseBits(n)
        self.assertEqual(expected_result, result)

    def test_reverse_bits_int_max(self):
        n = 4294967295
        expected_result = 4294967295
        result = self.solution.reverseBits(n)
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
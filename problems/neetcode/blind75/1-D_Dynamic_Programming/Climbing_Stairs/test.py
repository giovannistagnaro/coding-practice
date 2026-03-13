import unittest
from solution import Solution

class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climbing_stairs_example1(self):
        n = 2
        expected_result = 2
        result = self.solution.climbStairs(n)

        self.assertEqual(expected_result, result)

    def test_climbing_stairs_example2(self):
        n = 3
        expected_result = 3
        result = self.solution.climbStairs(n)

        self.assertEqual(expected_result, result)

    def test_climbing_stairs_single_step(self):
        n = 1
        expected_result = 1
        result = self.solution.climbStairs(n)

        self.assertEqual(expected_result, result)

    def test_climbing_stairs_higher(self):
        n = 7
        expected_result = 21
        result = self.solution.climbStairs(n)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
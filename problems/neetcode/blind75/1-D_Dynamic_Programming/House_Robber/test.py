import unittest
from solution import Solution

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_house_robber_example1(self):
        nums = [1,1,3,3]
        expected_result = 4
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_example2(self):
        nums = [2,9,8,3,6]
        expected_result = 16
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_no_houses(self):
        nums = []
        expected_result = 0
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_one_house(self):
        nums = [5]
        expected_result = 5
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_two_houses(self):
        nums = [9, 3]
        expected_result = 9
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_big(self):
        nums = [1, 1, 2, 3, 5, 8, 13, 200]
        expected_result = 212
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_winner_all_ones(self):
        nums = [1, 1, 1, 1, 1, 1, 1]
        expected_result = 4
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
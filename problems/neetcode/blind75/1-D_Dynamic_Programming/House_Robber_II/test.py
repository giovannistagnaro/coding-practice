import unittest
from solution import Solution

class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_house_robber_ii_example1(self):
        nums = [3,4,3]
        expected_result = 4
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_ii_example2(self):
        nums = [2,9,8,3,6]
        expected_result = 15
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_ii_single_home(self):
        nums = [20]
        expected_result = 20
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

    def test_house_robber_ii_self_loop(self):
        nums = [3, 1]
        expected_result = 3
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)


    def test_house_robber_ii_self_loop_ii(self):
        nums = [1, 3]
        expected_result = 3
        result = self.solution.rob(nums)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
    
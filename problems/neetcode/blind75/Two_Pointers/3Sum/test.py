import unittest
from solution import Solution

class Test3Sum(unittest.TestCase):
    def equal_ignore_all_order(self, a: list[list[int]], b: list[list[int]]) -> bool:
        normalize = lambda x: sorted(tuple(sorted(inner)) for inner in x)
        return normalize(a) == normalize(b)

    def setUp(self):
        self.solution = Solution()

    def test_3sum_example1(self):
        nums = [-1,0,1,2,-1,-4]
        expected_result = [[-1,-1,2],[-1,0,1]]
        result = self.solution.threeSum(nums)
        self.assertTrue(self.equal_ignore_all_order(expected_result, result))

    def test_3sum_example2(self):
        nums = [0,1,1]
        expected_result = []
        result = self.solution.threeSum(nums)
        self.assertTrue(self.equal_ignore_all_order(expected_result, result))

    def test_3sum_example3(self):
        nums = [0,0,0]
        expected_result = [[0,0,0]]
        result = self.solution.threeSum(nums)
        self.assertTrue(self.equal_ignore_all_order(expected_result, result))


    def test_3sum_one(self):
        nums = [-2, 2, 0, 5, 10, 15, 20]
        expected_result = [[-2, 2, 0]]
        result = self.solution.threeSum(nums)
        self.assertTrue(self.equal_ignore_all_order(expected_result, result))

if __name__ == "__main__":
    unittest.main()
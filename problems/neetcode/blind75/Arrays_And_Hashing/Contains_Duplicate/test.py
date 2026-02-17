import unittest
from solution import Solution

class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_contains_dup_example1(self):
        nums = [1, 2, 3, 3]
        result = self.solution.hasDuplicate(nums)
        self.assertTrue(result)

    def test_contains_dup_example2(self):
        nums = [1, 2, 3, 4]
        result = self.solution.hasDuplicate(nums)
        self.assertFalse(result)

    def test_contains_dup_same_number(self):
        nums = [1, 1, 1, 1]
        result = self.solution.hasDuplicate(nums)
        self.assertTrue(result)

    def test_contains_dup_same_no_numbers(self):
        nums = []
        result = self.solution.hasDuplicate(nums)
        self.assertFalse(result)

    def test_contains_dup_first_last(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        result = self.solution.hasDuplicate(nums)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
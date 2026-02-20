import unittest
from solution import Solution

class TestProductsOfArrayExceptSelf(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_products_of_array_except_self_example1(self):
        nums = [1, 2, 4, 6]
        expected = [48, 24, 12, 8]
        result = self.solution.productExceptSelf(nums)

        self.assertEqual(expected, result)

    def test_products_of_array_except_self_example2(self):
        nums = [-1,0,1,2,3]
        expected = [0,-6,0,0,0]
        result = self.solution.productExceptSelf(nums)

        self.assertEqual(expected, result)

    def test_products_of_array_except_self_ones(self):
        nums = [1, 1, 1, 1, 1]
        expected = [1, 1, 1, 1, 1]
        result = self.solution.productExceptSelf(nums)

        self.assertEqual(expected, result)

    def test_products_of_array_except_self_zeros(self):
        nums = [0, 0]
        expected = [0, 0]
        result = self.solution.productExceptSelf(nums)

        self.assertEqual(expected, result)

    def test_products_of_array_except_self_fib(self):
        nums = [1, 1, 2, 3, 5, 7]
        expected = [210, 210, 105, 70, 42, 30]
        result = self.solution.productExceptSelf(nums)

        self.assertEqual(expected, result)
        
if __name__ == "__main__":
    unittest.main()    
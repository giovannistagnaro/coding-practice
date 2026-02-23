import unittest
from solution import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_container_with_most_water_example1(self):
        height = [1,7,2,5,4,7,3,6]
        expected_result = 36
        result = self.solution.maxArea(height)
        self.assertEqual(expected_result, result)

    def test_container_with_most_water_example2(self):
        height = [2,2,2]
        expected_result = 4
        result = self.solution.maxArea(height)
        self.assertEqual(expected_result, result)

    def test_container_with_most_water_zero(self):
        height = [0, 0, 0, 0]
        expected_result = 0
        result = self.solution.maxArea(height)
        self.assertEqual(expected_result, result)

    def test_container_with_most_water_rising(self):
        height = [1, 2, 3, 4, 5]
        expected_result = 6
        result = self.solution.maxArea(height)
        self.assertEqual(expected_result, result)
    
    def test_container_with_most_water_high_low(self):
        height = [1, 1, 1, 1, 10, 1, 1, 1, 1]
        expected_result = 8
        result = self.solution.maxArea(height)
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
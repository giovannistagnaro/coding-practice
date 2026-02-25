import unittest
from solution import Solution

class TestMinimumWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # self.solution_one = Solution_One()

    def test_minimum_window_substring_example1(self):
        s, t = "OUZODYXAZV", "XYZ"
        expected_result = "YXAZ"
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    def test_minimum_window_substring_example2(self):
        s, t = "xyz", "xyz"
        expected_result = "xyz"
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    def test_minimum_window_substring_example3(self):
        s, t = "x", "xy"
        expected_result = ""
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    def test_minimum_window_substring_mix(self):
        s, t = "XXxx", "xXx"
        expected_result = "Xxx"
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    def test_minimum_window_substring_one(self):
        s, t = "x", "x"
        expected_result = "x"
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    def test_minimum_window_substring_one_blank(self):
        s, t = "x", "y"
        expected_result = ""
        result = self.solution.minWindow(s, t)

        self.assertEqual(expected_result, result)

    # def test_minimum_window_substring_dict_matcher_not_sub(self):
    #     s, t = {"a": 5, "b": 2, "c": 0}, {"a": 5, "b": 2, "c": 1, "d": 3}
    #     result = self.solution_one.contains_sub_with_freqs(s, t)

    #     self.assertFalse(result)

    # def test_minimum_window_substring_dict_matcher_wrong_freqs(self):
    #     s, t = {"a": 5, "b": 2, "c": 0}, {"a": 5, "b": 2, "c": 1}
    #     result = self.solution_one.contains_sub_with_freqs(s, t)

    #     self.assertFalse(result)

    # def test_minimum_window_substring_dict_matcher_right_freqs(self):
    #     s, t = {"a": 5, "b": 2, "c": 1}, {"a": 5, "b": 2, "c": 1}
    #     result = self.solution_one.contains_sub_with_freqs(s, t)

    #     self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
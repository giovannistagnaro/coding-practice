import unittest
from solution import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = self.solution.groupAnagrams(strs)
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_example2(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        expected = [[""]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_example3(self):
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        expected = [["a"]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_all_same(self):
        strs = ["abc", "bca", "cba"]
        result = self.solution.groupAnagrams(strs)
        expected = [["abc", "bca", "cba"]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

if __name__ == "__main__":
    unittest.main()
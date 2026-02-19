import unittest
from solution import Solution

class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams_example1(self):
        strs = ["act","pots","tops","cat","stop","hat"]
        result = self.solution.groupAnagrams(strs)
        expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_example2(self):
        strs = ["x"]
        result = self.solution.groupAnagrams(strs)
        expected = [["x"]]

        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)


    def test_group_anagrams_example3(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        expected = [[""]]
        
        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_same_word(self):
        strs = ["cat", "cat", "cat", "cat", "cat"]
        result = self.solution.groupAnagrams(strs)
        expected = [["cat", "cat", "cat", "cat", "cat"]]
        
        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)

    def test_group_anagrams_no_anagrams(self):
        strs = ["abc", "def", "ghi", "jkl"]
        result = self.solution.groupAnagrams(strs)
        expected = [["abc"], ["def"], ["ghi"], ["jkl"]]
        
        expected_set = {frozenset(sublist) for sublist in expected}
        result_set = {frozenset(sublist) for sublist in result}
        self.assertEqual(result_set, expected_set)      

if __name__ == "__main__":
    unittest.main()
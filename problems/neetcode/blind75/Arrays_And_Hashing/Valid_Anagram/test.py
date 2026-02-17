import unittest
from solution import Solution

class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_is_anagram_example1(self):
        s = "racecar"
        t = "carrace"
        result = self.solution.isAnagram(s, t)
        self.assertTrue(result)

    def test_is_anagram_example2(self):
        s = "jar"
        t = "jam"
        result = self.solution.isAnagram(s, t)
        self.assertFalse(result)

    def test_is_anagram_empty(self):
        s = ""
        t = ""
        result = self.solution.isAnagram(s, t)
        self.assertTrue(result)
    
    def test_is_anagram_one_empty(self):
        s = ""
        t = "ducks"
        result = self.solution.isAnagram(s, t)
        self.assertFalse(result)

    def test_is_anagram_close(self):
        s = "abcdefghijklmnop"
        t = "ponmlkjihgfedcbb"
        result = self.solution.isAnagram(s, t)
        self.assertFalse(result)

    def test_is_anagram_one_char(self):
        s = "c"
        t = "c"
        result = self.solution.isAnagram(s, t)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
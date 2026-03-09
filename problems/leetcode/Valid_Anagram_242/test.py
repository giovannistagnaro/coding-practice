import unittest
from solution import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_anagram_example1(self):
        s, t = "anagram", "nagaram"
        result = self.solution.isAnagram(s, t)

        self.assertTrue(result)

    def test_valid_anagram_example2(self):
        s, t = "rat", "car"
        result = self.solution.isAnagram(s, t)

        self.assertFalse(result)


    def test_valid_anagram_single(self):
        s, t = "a", "a"
        result = self.solution.isAnagram(s, t)

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
import unittest
from solution import RandomizedSet

class TestInsertDeleteGetRandom(unittest.TestCase):
    def setUp(self):
        self.randomizedSet = RandomizedSet()
    
    def test_insert_delete_example1(self):
        self.assertTrue(self.randomizedSet.insert(1))
        self.assertFalse(self.randomizedSet.remove(2))
        self.assertTrue(self.randomizedSet.insert(2))
        self.assertTrue(self.randomizedSet.getRandom() in {1, 2})
        self.assertTrue(self.randomizedSet.remove(1))
        self.assertFalse(self.randomizedSet.insert(2))
        self.assertEqual(self.randomizedSet.getRandom(), 2)

if __name__ == "__main__":
    unittest.main()
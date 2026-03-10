import unittest
from solution import RandomizedCollection

class TestInsertDeleteGetRandom(unittest.TestCase):
    def setUp(self):
        self.randomizedCollection = RandomizedCollection()
    
    def test_insert_delete_example1(self):
        self.assertTrue(self.randomizedCollection.insert(1))
        self.assertFalse(self.randomizedCollection.insert(1))
        self.assertTrue(self.randomizedCollection.insert(2))
        self.assertTrue(self.randomizedCollection.getRandom() in {1, 2})
        self.assertTrue(self.randomizedCollection.remove(1))
        self.assertTrue(self.randomizedCollection.getRandom() in {1, 2})

if __name__ == "__main__":
    unittest.main()
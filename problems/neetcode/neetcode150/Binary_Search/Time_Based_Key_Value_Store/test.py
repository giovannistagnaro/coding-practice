import unittest
from solution import TimeMap

class TestTimebasedKeyValueStore(unittest.TestCase):
    def test_time_based_k_v_store_example(self):
        timeMap = TimeMap()
        timeMap.set("alice", "happy", 1)
        self.assertEqual(timeMap.get("alice", 1), "happy")
        self.assertEqual(timeMap.get("alice", 2), "happy")
        timeMap.set("alice", "sad", 3)
        self.assertEqual(timeMap.get("alice", 3), "sad")

    def test_time_based_k_v_store_test(self):
        timeMap = TimeMap()
        timeMap.set("test", "one", 10)
        timeMap.set("test", "two", 20)
        timeMap.set("test", "three", 30)

        self.assertEqual(timeMap.get("test", 15), "one")
        self.assertEqual(timeMap.get("test", 25), "two")
        self.assertEqual(timeMap.get("test", 35), "three")

if __name__ == "__main__":
    unittest.main()
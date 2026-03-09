import unittest
from solution import HitCounter

class TestHitCounter(unittest.TestCase):
    def setUp(self):
        self.hitCounter = HitCounter()

    def test_hit_counter_all_same(self):
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        result = self.hitCounter.getHits(300)
        self.assertEqual(result, 5)

    def test_hit_counter_all_same_none(self):
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        result = self.hitCounter.getHits(3000)
        self.assertEqual(result, 0)

    def test_hit_counter_separated(self):
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1000)
        self.hitCounter.hit(1000)
        result = self.hitCounter.getHits(1200)
        self.assertEqual(result, 2)

    def test_hit_counter_off_by_one(self):
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1)
        self.hitCounter.hit(1000)
        self.hitCounter.hit(1000)
        result = self.hitCounter.getHits(1300)
        self.assertEqual(result, 0)

    def test_hit_counter_off_by_one(self):
        result = self.hitCounter.getHits(100)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
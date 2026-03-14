import unittest
from solution import MedianFinder
class TestFindMedian(unittest.TestCase):
    def setUp(self):
        self.medianFinder = MedianFinder()

    def test_median_finder(self):
        # [1,2,3,4,5,6]
        self.medianFinder.addNum(1)    # arr = [1]
        self.assertEqual(self.medianFinder.findMedian(), 1)
        self.medianFinder.addNum(3)    # arr = [1, 3]
        self.assertEqual(self.medianFinder.findMedian(), 2.0)
        self.medianFinder.addNum(2)    # arr[1, 2, 3]
        self.assertEqual(self.medianFinder.findMedian(), 2)
        self.medianFinder.addNum(8)    # arr[1, 2, 3, 8]
        self.assertEqual(self.medianFinder.findMedian(), 2.5)
        self.medianFinder.addNum(-19)  # arr[-19, 1, 2, 3, 8]
        self.assertEqual(self.medianFinder.findMedian(), 2)

if __name__ == "__main__":
    unittest.main()
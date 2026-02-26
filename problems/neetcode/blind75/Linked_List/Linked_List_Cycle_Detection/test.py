import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestLinkedListCycleDetection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_linked_list_cycle_detection_example1(self):
        b = ListNode(2, None)
        d = ListNode(4, b)
        c = ListNode(3, d)
        b.next = c
        a = ListNode(1, b)

        result = self.solution.hasCycle(a)
        self.assertTrue(result)

    def test_linked_list_cycle_detection_example2(self):
        b = ListNode(2, None)
        a = ListNode(1, b)

        result = self.solution.hasCycle(a)
        self.assertFalse(result)

    def test_linked_list_cycle_detection_empty(self):
        a = None

        result = self.solution.hasCycle(a)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
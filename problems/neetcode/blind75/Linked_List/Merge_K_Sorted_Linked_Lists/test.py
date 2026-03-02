import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestMergeKSortedLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_k_lists_example1(self):
        c1 = ListNode(4, None)
        b1 = ListNode(2, c1)
        a1 = ListNode(1, b1)

        c2 = ListNode(5, None)
        b2 = ListNode(3, c2)
        a2 = ListNode(1, b2)

        b3 = ListNode(6, None)
        a3 = ListNode(3, b3)

        result = self.solution.mergeKLists([a1,a2,a3])
        expected_result = [1,1,2,3,3,4,5,6]

        for i in range(len(expected_result)):
            self.assertEqual(result.val, expected_result[i])
            result = result.next
        self.assertIsNone(result)

    def test_merge_k_lists_example2(self):
        result = self.solution.mergeKLists(None)
        self.assertIsNone(result)

    def test_merge_k_lists_example3(self):
        result = self.solution.mergeKLists([None])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestMergeTwoSortedLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_two_sorted_linked_lists_example1(self):
        c1 = ListNode(4, None)
        b1 = ListNode(2, c1)
        a1 = ListNode(1, b1)

        c2 = ListNode(5, None)
        b2 = ListNode(3, c2)
        a2 = ListNode(1, b2)

        result = self.solution.mergeTwoLists(a1, a2)
        expected_result = [1,1,2,3,4,5]
        try:
            for i in range(len(expected_result)):
                self.assertEqual(result.val, expected_result[i])
                result = result.next
        except:
            self.fail("Error accessing value of result")

    def test_merge_two_sorted_linked_lists_example2(self):
        a1 = None

        b2 = ListNode(2, None)
        a2 = ListNode(1, b2)

        result = self.solution.mergeTwoLists(a1, a2)
        expected_result = [1,2]
        try:
            for i in range(len(expected_result)):
                self.assertEqual(result.val, expected_result[i])
                result = result.next
        except:
            self.fail("Error accessing value of result")

    def test_merge_two_sorted_linked_lists_example3(self):
        a1 = None
        a2 = None

        self.assertIsNone(self.solution.mergeTwoLists(a1, a2))

if __name__ == "__main__":
    unittest.main()
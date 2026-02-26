import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_linked_list_example1(self):
        d = ListNode(0, None)
        c = ListNode(1, d)
        b = ListNode(2, c)
        a = ListNode(3, b)
        result = self.solution.reverseList(a)
        expected_result = d

        self.assertEqual(result, expected_result)
        self.assertIsNone(a.next)
        self.assertEqual(b.next, a)
        self.assertEqual(c.next, b)
        self.assertEqual(d.next, c)

    def test_reverse_linked_list_example2(self):
        head = None
        result = self.solution.reverseList(head)

        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
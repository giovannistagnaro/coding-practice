import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reorder_list_example1(self):
        d = ListNode(8, None)
        c = ListNode(6, d)
        b = ListNode(4, c)
        a = ListNode(2, b)

        expected_result = [2,8,4,6]
        self.solution.reorderList(a)

        i = 0
        while a:
            self.assertEqual(a.val, expected_result[i])
            a = a.next
            i += 1

        self.assertIsNone(a)

    def test_reorder_list_example2(self):
        e = ListNode(10, None)
        d = ListNode(8, e)
        c = ListNode(6, d)
        b = ListNode(4, c)
        a = ListNode(2, b)

        expected_result = [2,10,4,8,6]
        self.solution.reorderList(a)

        i = 0
        while a:
            self.assertEqual(a.val, expected_result[i])
            a = a.next
            i += 1

        self.assertIsNone(a)

    def test_reorder_list_single(self):
        a = ListNode(2, None)

        expected_result = [2]
        self.solution.reorderList(a)

        i = 0
        while a:
            self.assertEqual(a.val, expected_result[i])
            a = a.next
            i += 1

        self.assertIsNone(a)

if __name__ == "__main__":
    unittest.main()
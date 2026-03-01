import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from ListNode import ListNode

class TestRemoveNodeFromEndOfLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_from_end_example1(self):
        d = ListNode(8, None)
        c = ListNode(6, d)
        b = ListNode(4, c)
        a = ListNode(2, b)

        expected_result = [2,4,8]
        result = self.solution.removeNthFromEnd(a, 2)

        i = 0
        while result:
            self.assertEqual(result.val, expected_result[i])
            result = result.next
            i += 1

        self.assertIsNone(result)

    def test_remove_from_end_example2(self):
        e = ListNode(10, None)

        result = self.solution.removeNthFromEnd(e, 1)
        self.assertIsNone(result)

    def test_remove_from_end_example3(self):
        b = ListNode(2, None)
        a = ListNode(1, None)

        expected_result = [2]
        result = self.solution.removeNthFromEnd(a, 2)

        i = 0
        while result:
            self.assertEqual(result.val, expected_result[i])
            result = result.next
            i += 1

        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ListNode import ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_list1 = list1
        curr_list2 = list2
        dummy = ListNode(0, None)
        dummy_head = dummy
        combined_list = dummy

        while curr_list1 or curr_list2:
            if not curr_list1:
                combined_list.next = curr_list2
                combined_list = combined_list.next
                curr_list2 = curr_list2.next
            elif not curr_list2:
                combined_list.next = curr_list1
                combined_list = combined_list.next
                curr_list1 = curr_list1.next
            elif curr_list1.val <= curr_list2.val:
                combined_list.next = curr_list1
                combined_list = combined_list.next
                curr_list1 = curr_list1.next
            else:
                combined_list.next = curr_list2
                combined_list = combined_list.next
                curr_list2 = curr_list2.next
        
        return dummy_head.next

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ListNode import ListNode
from typing import Optional, List

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwoLists(list1, list2):
            curr = dummy = ListNode(0, None)

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            curr.next = list1 or list2

            return dummy.next
        
        
        for i in range(1, len(lists), 1):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
            
        return lists[len(lists) - 1]
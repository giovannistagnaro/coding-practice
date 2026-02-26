import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ListNode import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        prev_prev = prev = None
        curr = head

        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = prev_prev
            prev_prev = prev
        curr.next = prev

        return curr
        
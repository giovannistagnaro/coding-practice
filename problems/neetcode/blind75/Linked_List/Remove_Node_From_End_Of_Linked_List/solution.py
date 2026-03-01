import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ListNode import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next
        
        if count == n:
            return head.next
        elif count == 1:
            return None
        
        prev = head
        for _ in range(count - n - 1):
            prev = prev.next

        if prev.next:
            prev.next = prev.next.next
        else:
            del prev

        return head
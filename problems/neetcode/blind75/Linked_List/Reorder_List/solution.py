import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ListNode import ListNode
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        def rev_list(start: ListNode):
            prev, curr = None, start
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        list_size = 0
        counter = head
        while counter:
            list_size += 1
            counter = counter.next

        if list_size == 1:
            return
        
        mid = list_size // 2

        front = dummy_back = head
        dummy_prev = None
        for _ in range(mid):
            dummy_prev = dummy_back
            dummy_back = dummy_back.next

        back = ListNode(dummy_back.val, dummy_back.next)
        dummy_prev.next = None

        back = rev_list(back)

        while front and back:
            temp_f = front.next
            temp_b = back.next
            front.next = back
            back.next = temp_f if temp_f else temp_b
            front = temp_f
            back = temp_b
        
        if temp_f:
            front.next = temp_f
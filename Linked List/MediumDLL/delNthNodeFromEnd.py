'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        for i in range(n):
            p2 = p2.next
        
        while p2 and p2.next :
            p2 = p2.next
            p1 = p1.next

        if p2 is None and p1 == head:
            return head.next
        else :
            print(p1.val)
            p1.next = p1.next.next
    
        return head
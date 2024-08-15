'''Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        mid = head
        while temp and temp.next:
            temp = temp.next.next
            mid = mid.next
        
        return mid
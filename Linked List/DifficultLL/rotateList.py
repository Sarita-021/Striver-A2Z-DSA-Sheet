'''Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
https://leetcode.com/problems/rotate-list/description/ '''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 1
        if head is None or head.next is None or k == 0:
            return head
        while temp.next:
            cnt += 1
            temp = temp.next
        
        if k%cnt == 0:
            return head
        
        temp.next = head
        k = k%cnt
        newHeadLoc = cnt - k
        while newHeadLoc > 0:
            newHeadLoc -= 1
            temp = temp.next
        
        newHead = temp.next
        temp.next = None
        return newHead

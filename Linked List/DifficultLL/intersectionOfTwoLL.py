'''Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
https://leetcode.com/problems/intersection-of-two-linked-lists/description/ '''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        dummy1, dummy2 = headA, headB

        while dummy1 != dummy2:
            dummy1 = dummy1.next if dummy1 else headB
            dummy2 = dummy2.next if dummy2 else headA

        return dummy1
        
# This is based on the same principle as 3 + 2 = 5 and 2 + 3 = 5.
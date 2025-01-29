'''Given the head of a linked list, return the list after sorting it in ascending order.'''


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeTwoSortedLinkedLists(list1, list2):
    dummyNode = ListNode(-1)
    temp = dummyNode

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next 

    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    
    return dummyNode.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        middle = findMiddle(head)

        right = middle.next
        middle.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)
        return mergeTwoSortedLinkedLists(left, right)

        
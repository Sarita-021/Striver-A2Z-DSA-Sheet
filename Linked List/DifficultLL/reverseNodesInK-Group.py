'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not 
a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
https://leetcode.com/problems/reverse-nodes-in-k-group/description/ '''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_linked_list(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

def getKthNode(temp, k):
    k -= 1
    while temp is not None and k > 0:
        k -= 1
        temp = temp.next
    return temp

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = None
        while temp:
            kthNode = getKthNode(temp, k)
            if kthNode:
                if prevNode is None:
                    prevNode.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            reverse_linked_list(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
        return head

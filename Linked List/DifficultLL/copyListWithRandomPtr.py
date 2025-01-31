'''A linked list of length n is given such that each node contains an additional random pointer, which could point 
to any node in the list, or null.
https://leetcode.com/problems/copy-list-with-random-pointer/description/ '''


# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

                  
def insertCopyInBetween(head):
    temp = head
    while temp:
        nextElement = temp.next
        copy = Node(temp.val)
        copy.next = nextElement
        temp.next = copy
        temp = nextElement

def connectRandomPointers(head):
    temp = head
    while temp:
        copyNode = temp.next
        if temp.random:
            copyNode.random = temp.random.next
        else:
            copyNode.random = None

        temp = temp.next.next

def getDeepCopyList(head):
    temp = head
    dummyNode = Node(-1)
    res = dummyNode

    while temp:
        res.next = temp.next
        res = res.next
        temp.next = temp.next.next
        temp = temp.next

    return dummyNode.next


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        insertCopyInBetween(head)
        connectRandomPointers(head)
        return getDeepCopyList(head)
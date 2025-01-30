'''You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key 
if it is present and return the new DLL.'''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        if not head.next:
            if head.data == x :
                return head.next
            return head
        
        curr = head
        while curr.next:
            if curr.data == x:
                if curr == head:
                    head = curr.next
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
            curr = curr.next
        if curr.data == x:
            curr.prev.next = None
        return head
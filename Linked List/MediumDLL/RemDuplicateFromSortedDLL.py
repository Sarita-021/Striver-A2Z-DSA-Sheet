'''Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.
geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1 '''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        temp = head
        
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
                if temp.next is not None: temp.next.prev = temp
            else:
                temp = temp.next
        
        return head
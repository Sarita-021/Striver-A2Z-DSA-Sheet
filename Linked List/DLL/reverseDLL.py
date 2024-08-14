'''Given a doubly linked list of n elements. Your task is to reverse the doubly linked list in-place.'''


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        temp = head
        while temp :
            temp.next, temp.prev = temp.prev, temp.next
            head = temp
            temp = temp.prev
        
        return head
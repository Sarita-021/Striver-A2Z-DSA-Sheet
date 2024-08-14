'''Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.'''

# Node Class
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        head = curr = None
        for i in arr:
            temp = Node(i)
            
            if not head :
                head = curr = temp
            else :
                curr.next = temp
                temp.prev = curr
                curr = temp
        
        return head
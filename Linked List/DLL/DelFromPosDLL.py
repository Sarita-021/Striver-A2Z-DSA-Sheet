'''Given a doubly Linked list and a position. The task is to delete a node from a given position 
(position starts from 1) in a doubly linked list and return the head of the doubly Linked list.'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		
class Solution:
    def delete_node(self, head, x):
        temp = head
        pos = 1
        if x == 1:
            head = temp.next
            head.prev = None
            return head
            
        while pos < x-1 :
            temp = temp.next
            pos += 1
        
        temp.next = temp.next.next
        if temp.next :
            temp.next.prev = temp
        
        return head
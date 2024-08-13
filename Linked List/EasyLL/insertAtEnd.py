'''Given the head of a Singly Linked List and a value x, insert that value x at the end of the 
LinkedList and return the modified Linked List.'''

 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        temp = head
        new_node = Node(x)
        if not head:
            return new_node
            
        while temp.next :
            temp = temp.next
        
        temp.next = new_node
        
        return head
# Implement a Queue using Linked List.

# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.left = None
        self.right = None
    
    #Function to push an element into the queue.
    def push(self, item): 
        newNode = Node(item)
        if not self.left :
            self.left = self.right = newNode
        else:
            self.right.next = newNode
            self.right = newNode
    
    #Function to pop front element from the queue.
    def pop(self):
        if not self.left:
            return -1
        elif self.left == self.right:
            poppedItem = self.left.data
            self.left = self.right = None
            return poppedItem
        else:
            poppedItem = self.left.data
            self.left = self.left.next
            return poppedItem
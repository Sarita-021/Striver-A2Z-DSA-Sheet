

class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class MyStack:

    # # Constructor to initialize a node
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None 
        
    #Function to push an integer into the stack.
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode

    #Function to remove an item from top of the stack.
    def pop(self):
        if self.is_empty():
            return -1
        popped_data = self.top.data
        self.top = self.top.next  
        return popped_data
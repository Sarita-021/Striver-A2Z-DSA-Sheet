class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
    
class Solution:
    
    def constructLL(self, arr):
        root = None
        curr = None

        for item in arr:
            temp = Node(item)

            if not root:  # Handle empty list case efficiently
                root = curr = temp
            else:
                curr.next = temp
                curr = temp  # Update tail pointer for efficient appending

        return root
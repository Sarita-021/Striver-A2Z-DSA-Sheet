'''Given a linked list of n nodes and a key , the task is to check if the key is present in the linked list or not.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, n, head, key):
        if not head :
            return False
        
        temp = head
        while temp:
            if temp.data == key :
                return True
            temp = temp.next
        
        return False
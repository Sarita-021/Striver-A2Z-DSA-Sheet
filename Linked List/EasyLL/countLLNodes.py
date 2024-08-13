'''Given a singly linked list. The task is to find the length of the linked list, where length is defined 
as the number of nodes in the linked list.'''

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    def getCount(self, head):
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
            
        return cnt
'''Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at
the position just after pth node in the doubly linked list.'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    currIdx = 0
    temp = head
    newNode = Node(data)
    while currIdx < p :
        temp = temp.next
        currIdx += 1
    
    newNode.next = temp.next
    newNode.prev = temp
    if temp.next :
        temp.next.prev = temp.next = newNode
    else :
        temp.next = newNode
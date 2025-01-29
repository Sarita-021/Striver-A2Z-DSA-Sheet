'''Given a linked list where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked 
list such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the middle of 0s and 2s.
https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1 '''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next : return head
        zeroHead = zero = Node(0)
        oneHead = one = Node(0)
        twoHead = two =  Node(0)
        temp = head
        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1 :
                one.next = temp
                one = temp
            else :
                two.next = temp
                two = temp
            temp = temp.next
         
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
    
        # Updated head 
        head = zeroHead.next
        return head
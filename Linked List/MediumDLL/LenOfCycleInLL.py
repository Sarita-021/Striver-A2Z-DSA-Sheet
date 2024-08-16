'''Given the head of a linked list, determine whether the list contains a loop. If a 
loop is present, return the number of nodes in the loop, otherwise return 0.'''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        cnt = 0
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                slow = slow.next
                cnt += 1
                while slow != fast:
                    slow = slow.next
                    cnt += 1
                return cnt

        return cnt
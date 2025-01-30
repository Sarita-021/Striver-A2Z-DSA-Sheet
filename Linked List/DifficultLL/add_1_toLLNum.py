'''You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the
 number formed by concatinating all the list node numbers together and return the head of the modified linked list. 
 https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1 '''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self,head):
        temp = head
        nineCnt = 0
        cnt = 1
        
        while temp.next:
            if temp.next.data == 9:
                nineCnt += 1
            else :
                nineCnt = 0
            cnt += 1
            temp = temp.next
        
        st = cnt - nineCnt
        temp = head
        while st != 1:
            temp = temp.next
            st -= 1
        temp.data += 1
        while temp.next:
            temp = temp.next
            temp.data = 0
        return head
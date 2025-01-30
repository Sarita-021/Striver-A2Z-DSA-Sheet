'''Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list 
whose sum is equal to given value target.
https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1 '''

from typing import Optional
from typing import List

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None


class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        first = head
        second = head.next
        ans = []
        while second.next and (first.data + second.data < target):
            second = second.next
            
        while first != second and second.next != first:
            if (first.data + second.data) == target:
                ans.append((first.data, second.data))
                first = first.next
                second = second.prev
            elif (first.data + second.data) < target:
                first = first.next
            else:
                second = second.prev
                
        return ans
    

# Another approach using set

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        ans = []
        visited = set()
        currNode = head
    
        while currNode is not None:
            x = target - currNode.data
    
            if x in visited:
                ans.append([x, currNode.data])
    
            visited.add(currNode.data)
            currNode = currNode.next
    
        ans.sort(key=lambda pair: pair[0])
        return ans

'''You are given a stack St. You have to reverse the stack using recursion.'''

from typing import List

def bottomInsert(stack, num):
    if len(stack) == 0 :
        stack.append(num)
        return
    else:
        temp = stack.pop()
        bottomInsert(stack, num)
        stack.append(temp)

class Solution:
    def reverse(self,s): 
        if len(s) != 0:
            temp = s.pop()
            self.reverse(s)
            bottomInsert(s,temp)
'''Given a stack, the task is to sort it such that the top of the stack has the greatest element.
Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2

In Output 41 is the last element in the list i.e. at index -1. Since we are popping elements from the stack to print it is 
first in the output list. So, 41 is at the top of the stack. 32 is the second element in the list i.e. at index -2. So, 32 is
https://www.geeksforgeeks.org/problems/sort-a-stack/1 '''

def sortedInsert(stack, num):
    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
        return
    else:
        temp = stack.pop()
        sortedInsert(stack, num)
        stack.append(temp)


class Solution:
    def Sorted(self, s):
        # Code here
        if len(s) != 0:
            temp = s.pop()
            self.Sorted(s)
            sortedInsert(s,temp)
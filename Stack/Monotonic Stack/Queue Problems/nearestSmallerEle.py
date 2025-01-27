'''Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the
 element has an index smaller than i.
More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
'''

from typing import List


class Solution:
    def prevSmaller(self, A: List[int]) -> List[int]:
        s = [A[0]]
        res = []
        
        for i in range(len(A)):
            if A[i] > s[-1] :
                res.append(s[-1])
            else:
                while s and A[i] <= s[-1]:
                    s.pop()
                if not s:
                    res.append(-1)
                else :
                    res.append(s[-1])
            s.append(A[i])

        return res
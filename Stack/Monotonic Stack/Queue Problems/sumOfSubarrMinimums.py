'''Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
 Since the answer may be large, return the answer modulo 109 + 7.
 https://leetcode.com/problems/sum-of-subarray-minimums/description/ '''

from typing import List



class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + arr + [-inf]
        s = []
        MOD = 10**9+7
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res = (res + (A[j] * (i - j) * (j - k)) % MOD) % MOD
            s.append(i)
        return res
    

# Another approach


def prevSmallerEqual(A):
    s = []
    res = []
    
    for i in range(len(A)):
        while s and A[i] < A[s[-1]]:
            s.pop()
        if not s:
            res.append(-1)
        else :
            res.append(s[-1])
        s.append(i)

    return res

def nextSmaller(A):
    s = []
    res = []
    
    for i in range(len(A)-1,-1,-1):
        while s and A[i] <= A[s[-1]]:
            s.pop()
        if not s:
            res.append(len(A))
        else :
            res.append(s[-1])
        s.append(i)

    return res[::-1]

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pse = prevSmallerEqual(arr)
        nse = nextSmaller(arr)
        print(pse)
        print(nse)
        total = 0
        MOD = 10**9+7
        for i in range(len(arr)):
            l = i - pse[i]
            r = nse[i] - i 
            total = (total + (r * l * arr[i]) % MOD) % MOD
        return total
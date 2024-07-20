'''Given an unsorted array arr of size n of positive integers. One number 'A' 
from set {1, 2,....,N} is missing and one number 'B' occurs twice in array. Find these two numbers.'''


class Solution:
    def findTwoElement( self,arr, n): 
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        S, S2 = 0, 0
        for i in range(n):
            S += arr[i]
            S2 += arr[i] * arr[i]
        val1 = S - SN
        val2 = S2 - S2N
        val2 = val2 // val1
        x = (val1 + val2) // 2
        y = x - val1
    
        return [x, y]
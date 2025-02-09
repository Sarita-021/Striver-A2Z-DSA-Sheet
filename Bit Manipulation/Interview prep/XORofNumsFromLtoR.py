'''You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].
Input: 
L = 4, R = 8 
Output:
8 
Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1?'''

class Solution:
    def findXOR(self, l, r):
        def xorTillN(n):
            if (n%4) == 1: return 1
            elif (n%4) == 2 : return n+1
            elif (n%4) == 3 : return 0
            else : return n
        
        lxor = xorTillN(l-1)
        rxor = xorTillN(r)
        return lxor^rxor

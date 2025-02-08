'''Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false 
if the number is odd.
https://www.geeksforgeeks.org/problems/odd-or-even3618/1'''

class Solution:
    def isEven(self, n):
        return  n&1 == 0 
    

'''Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
https://leetcode.com/problems/power-of-two/description/'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & n-1 == 0
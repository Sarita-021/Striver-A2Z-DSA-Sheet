'''You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive).
https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1'''

# Optimized solution : Brian Kernighan's approach

import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        
        if n == 0:
            return 0
        
        # Find the largest power of 2 (<= n)
        x = int(math.log2(n))
        
        # Count bits up to 2^x - 1
        bits_up_to_2x = x * (1 << (x - 1)) if x > 0 else 0
        
        # Count MSB in remaining numbers
        msb_count = n - (1 << x) + 1
        
        # Recur for remaining numbers
        remaining = self.countSetBits(n - (1 << x))
        
        return bits_up_to_2x + msb_count + remaining
        


# Less optimized solution

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        def cntSetBitsOfN(n):
            c = 0
            while n != 0:
                n = n&n-1
                c += 1
            return c
        
        cnt = 0
        for i in range(1, n+1):
            cnt += cntSetBitsOfN(i)
        
        return cnt
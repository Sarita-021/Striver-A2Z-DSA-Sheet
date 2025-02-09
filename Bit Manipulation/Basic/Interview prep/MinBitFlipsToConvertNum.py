'''A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/ '''

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = (start^goal)
        cnt = 0
        while num != 0:
            if num&1 == 1:
                cnt += 1
            num = num >> 1
            
        return cnt
'''Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).'''

class Solution:
    def floorSqrt(self, x): 
        mn = 1
        mx = x//2 + 1
        while mn <= mx :
            mid = (mn+mx)//2
            if mid*mid <= x:
                mn = mid+1
            else :
                mx = mid-1
        return mx
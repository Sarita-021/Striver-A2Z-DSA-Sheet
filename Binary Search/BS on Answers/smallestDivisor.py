'''Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
divide all the array by it, and sum the division's result. Find the smallest divisor such that the result 
mentioned above is less than or equal to threshold.'''

from math import ceil
from typing import List


def cntThold(nums, td):
    cnt = 0
    for i in range(len(nums)):
        cnt += ceil(nums[i]/td)
    return cnt

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = -1
        while low <= high :
            mid = (low+high)//2
            tthd = cntThold(nums, mid)
            if tthd <= threshold :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans
'''Given an integer array nums, find the 
subarray with the largest sum, and return its sum.'''

from cmath import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -inf
        currsum = 0
        for i in nums:
            currsum += i
            if currsum > maxsum:
                maxsum = currsum
            if currsum < 0 :
                currsum = 0

        return maxsum

'''Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = len(nums)+1
        s = 0
        l = 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target :
                minlen = min(minlen, i-l+1)
                print(minlen, s, l)
                s -= nums[l]
                l += 1
        if minlen == len(nums)+1:
            return 0
        return minlen
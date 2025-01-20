'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        nums.sort()
        maxlen = 1
        tmpcnt = 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                tmpcnt += 1
            elif nums[i-1] == nums[i]:
                continue
            else :
                tmpcnt = 1
            
            maxlen = max(maxlen, tmpcnt)
        return maxlen

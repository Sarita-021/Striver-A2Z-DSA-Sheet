'''Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each 
unique element appears at most twice. The relative order of the elements should be kept the same.'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[k] and cnt < 2:
                cnt += 1
                k += 1
            elif nums[i] != nums[k]:
                cnt = 1
                k += 1
            nums[i], nums[k] = nums[k], nums[i]

        return k+1
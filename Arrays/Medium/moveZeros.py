# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        iz = 0
        for i in range(0,len(nums)):
            if (nums[i] == 0):
                continue
            nums[iz],nums[i] = nums[i],nums[iz]
            iz+= 1
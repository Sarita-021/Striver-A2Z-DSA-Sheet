# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSumMap = {}
        for i in range(0,len(nums)):
            num = nums[i]
            rem = target - num
            if rem in prevSumMap :
                return [prevSumMap[rem], i]

            if num not in prevSumMap :
                prevSumMap[num] = i

        return
        
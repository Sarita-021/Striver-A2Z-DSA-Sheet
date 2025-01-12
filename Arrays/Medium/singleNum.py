# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total_sum = 0

        for i in nums:
            total_sum = total_sum ^ i
            
        return total_sum
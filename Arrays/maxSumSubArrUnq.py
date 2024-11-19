'''You are given an integer array nums and an integer k. Find the maximum subarray sum of all the 
subarrays of nums that meet the following conditions:
-The length of the subarray is k, and
-All the elements of the subarray are distinct.
-Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.'''

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        current_sum = 0
        max_sum = 0
        begin = 0

        for end in range(n): 
            if nums[end] not in elements:
                current_sum += nums[end]
                elements.add(nums[end])

                if end - begin + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
                
                begin += 1

        return max_sum
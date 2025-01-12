'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  
        
        for num in nums:
            prefix_sum += num  
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  
            else:
                prefix_sum_count[prefix_sum] = 1  
        
        return count
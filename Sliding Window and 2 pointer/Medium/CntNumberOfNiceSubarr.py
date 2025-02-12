'''Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
https://leetcode.com/problems/count-number-of-nice-subarrays/'''

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(goal):
            if goal < 0: return 0  # No valid subarrays if goal is negative
            l = s = count = 0
            for r in range(len(nums)):
                s += nums[r]%2      # Add 1 if nums[r] is odd else 0
                while s > goal:  # Shrink window if sum exceeds goal
                    s -= nums[l]%2      # Subtract 1 if nums[l] is odd else 0
                    l += 1
                count += r - l + 1  # Count all valid subarrays ending at 'r'
            return count

        return atMost(k) - atMost(k - 1)
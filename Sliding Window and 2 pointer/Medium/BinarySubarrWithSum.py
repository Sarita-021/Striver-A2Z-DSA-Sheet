'''Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
https://leetcode.com/problems/binary-subarrays-with-sum/description/'''


from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0: return 0  # No valid subarrays if goal is negative
            l = s = count = 0
            for r in range(len(nums)):
                s += nums[r]
                while s > goal:  # Shrink window if sum exceeds goal
                    s -= nums[l]
                    l += 1
                count += r - l + 1  # Count all valid subarrays ending at 'r'
            return count

        return atMost(goal) - atMost(goal - 1)

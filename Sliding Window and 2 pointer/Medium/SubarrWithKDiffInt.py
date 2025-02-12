'''Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
https://leetcode.com/problems/subarrays-with-k-different-integers/'''


from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(goal):
            """
            Returns the number of subarrays that contain at most 'goal' distinct integers.
            Uses a sliding window approach to efficiently count valid subarrays.
            """
            l = count = 0  # Left pointer and total count of valid subarrays
            int_cnt = defaultdict(int)  # Dictionary to store the frequency of elements

            for r in range(len(nums)):  # Expanding the right boundary of the window
                int_cnt[nums[r]] += 1  # Add the current element to the count
                
                # If we have more than 'goal' distinct elements, shrink the left boundary
                while len(int_cnt) > goal:
                    int_cnt[nums[l]] -= 1  # Reduce the count of the leftmost element
                    if int_cnt[nums[l]] == 0:
                        int_cnt.pop(nums[l])  # Remove it completely if count reaches 0
                    l += 1  # Move the left pointer forward
                
                count += l  # Add the number of valid subarrays ending at index r

            return count

        # The number of subarrays with exactly k distinct elements is:
        # Subarrays with at most k distinct - Subarrays with at most (k-1) distinct
        return atMost(k) - atMost(k - 1)

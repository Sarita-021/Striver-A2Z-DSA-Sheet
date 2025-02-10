'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if 
you can flip at most k 0's.
https://leetcode.com/problems/max-consecutive-ones-iii/description/'''


from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0  # Left pointer
        z = 0  # Count of zeros in the window

        for r in range(len(nums)):  # Expanding right pointer
            if nums[r] == 0:
                z += 1
            
            # If we exceed allowed zero count, shrink the window
            if z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1  # Move left pointer

        return r - l + 1  # Since 'r' stops at the last index


# This is slightly less optimized version of the above code but it's easier to understand

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        maxlen = 0
        z = 0
        while r < len(nums):
            if nums[r] == 0:
                z += 1
            if z > k:
                while z > k:
                    if nums[l] == 0:
                        z -= 1
                    l += 1

            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
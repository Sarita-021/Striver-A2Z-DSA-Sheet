"""Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue. We will use the 
integers 0, 1, and 2 to represent the color red, white, and blue, respectively."""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = i = 0
        r = len(nums) - 1
        while i <= r :
            if nums[i] == 0 :
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2 :
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            
            i += 1


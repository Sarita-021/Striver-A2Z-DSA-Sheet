'''Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150 '''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right :
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
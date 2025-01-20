'''A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.'''

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        if len(nums) == 0 or len(nums)==1:
            return 0
        if nums[0] > nums[1] :
            return 0
        elif nums[-2] < nums[-1] :
            return len(nums)-1
        while low <= high :
            mid = (low+high)//2
            if nums[mid-1] < nums[mid] > nums[mid+1] :
                return mid
            if (mid-1) >= 0 :
                if nums[mid-1] < nums[mid] < nums[mid+1] :
                    low = mid+1
                else :
                    high = mid-1
            else :
                low = mid+1
            
        return -1
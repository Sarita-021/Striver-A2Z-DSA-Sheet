'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high :
            mid = (low+high)//2
            if target <= nums[mid] :
                high = mid-1
            else :
                low = mid+1
        return high+1
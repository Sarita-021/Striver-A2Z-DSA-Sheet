'''Given the sorted rotated array nums of unique elements, return the minimum element of this array.'''

from typing import List


def minEle(nums, low, high, ans) :
    mid = (low+high)//2
    if (low > high) :
        return ans
    if nums[low] <= nums[mid] :
        ans = min(ans, nums[low])
        return minEle(nums, mid+1, high, ans)
    ans = min(ans, nums[mid])
    return minEle(nums, low, mid-1, ans)
            

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = inf
        return minEle(nums, low, high, ans)
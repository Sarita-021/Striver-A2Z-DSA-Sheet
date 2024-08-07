'''Given the array nums after the possible rotation and an integer target, return the index of 
target if it is in nums, or -1 if it is not in nums.'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high :
            mid = (low+high)//2
            if (nums[mid] == target) :
                return mid
            elif nums[low] <= nums[mid] <= nums[high] :
                if nums[mid] < target :
                    low = mid+1
                else :
                    high = mid-1
            elif (nums[low] >= nums[mid] <= nums[high]) :
                if (nums[high] >= target and nums[mid] <= target) :
                    low = mid+1
                else :
                    high = mid-1
            else :
                if (nums[low] <= target and nums[mid] >= target) :
                    high = mid-1
                else :
                    low = mid+1
        return -1


'''Other solution'''

def rsearch(nums, target, low, high) :
    mid = (low+high)//2
    if (low > high) :
        return -1
    elif nums[mid] == target :
        return mid
    elif nums[mid] >= nums[low]:
        if (nums[low] <= target and nums[mid] > target) :
            return rsearch(nums, target, low, mid-1)
        else :
            return rsearch(nums, target, mid+1, high)
    elif (nums[mid] < nums[high]) :
        if (nums[high] >= target and nums[mid] < target) :
            return rsearch(nums, target, mid+1, high)
    return rsearch(nums, target, low, mid-1)


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        ans = rsearch(nums, target, left, right)
        return ans
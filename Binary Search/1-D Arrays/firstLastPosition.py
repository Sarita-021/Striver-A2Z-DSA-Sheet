'''Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.'''

from typing import List


def libsearch(nums, target, left, right, ans) :
    if (left > right):
        return ans
    mid = (left+right)//2
    if nums[mid] >= target :
        if nums[mid] == target:
            ans = mid
        right = mid-1
        return libsearch(nums, target, left, right, ans)
    left = mid+1
    return libsearch(nums, target, left, right, ans)

def ribsearch(nums, target, left, right, ans) :
    if (left > right):
        return ans
    mid = (left+right)//2
    if nums[mid] <= target :
        if nums[mid] == target:
            ans = mid
        left = mid+1
        return ribsearch(nums, target, left, right, ans)
    right = mid-1
    return ribsearch(nums, target, left, right, ans)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, ans = 0, len(nums)-1, -1
        lowerIndex = libsearch(nums, target, left, right, ans)
        highIndex = ribsearch(nums, target, left, right, ans)
        return [lowerIndex, highIndex]
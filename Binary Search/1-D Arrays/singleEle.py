'''You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.'''

from typing import List


def findNonDup(nums, low, high):
    mid = (low+high)//2
    if (low >= high) :
        return nums[low]
    if mid%2 == 0 :
        if nums[mid] == nums[mid+1]:
            return findNonDup(nums, mid+1, high)
        elif nums[mid] == nums[mid-1]:
            return findNonDup(nums, low, mid-1)
    else :
        if nums[mid] == nums[mid+1]:
            return findNonDup(nums, low, mid-1)
        elif nums[mid] == nums[mid-1]:
            return findNonDup(nums, mid+1, high)
    return nums[mid]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        return findNonDup(nums, low, high)
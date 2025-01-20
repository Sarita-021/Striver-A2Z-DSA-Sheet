'''Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the 
largest sum of any subarray is minimized. Return the minimized largest sum of the split.'''


from typing import List


def cntSubarr(nums, limit) :
    cntSum = 0
    numOfSubarr = 1
    for i in nums :
        if cntSum + i <= limit :
            cntSum += i
        else :
            cntSum = i
            numOfSubarr += 1
    return numOfSubarr

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums,len(nums))
        while low <= high :
            mid = (low+high)//2
            subArr = cntSubarr(nums, mid)
            if subArr <= k :
                high = mid-1
            else :
                low = mid+1
        return low
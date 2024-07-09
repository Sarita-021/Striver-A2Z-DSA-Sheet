# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0
        tempcnt = 0
        for i in range(0,len(nums)):
            if (nums[i] == 1):
                tempcnt+=1
            else :
                maxCnt = max(maxCnt, tempcnt)
                tempcnt = 0
        maxCnt = max(maxCnt, tempcnt)
        return maxCnt
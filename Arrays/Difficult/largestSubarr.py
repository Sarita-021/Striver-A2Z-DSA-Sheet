'''Given an array having both positive and negative integers. 
The task is to compute the length of the largest subarray with sum 0.'''


class Solution:
    def maxLen(self, n, arr):
        preSum = maxLen = currLen = 0
        mapDic = {}
        for i in range(n):
            preSum += arr[i]
            if preSum == 0 :
                maxLen = i+1
            elif preSum in mapDic:
                currLen = i - mapDic[preSum]
                maxLen = max(currLen, maxLen)
            else :
                mapDic[preSum] = i
        return maxLen
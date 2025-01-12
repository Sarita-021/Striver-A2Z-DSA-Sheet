# Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        sum = 0
        maxLen = 0
        prevSumMap = {}
        for i in range(n):
            sum += arr[i]
            
            if (sum == k) :
                maxLen = max(maxLen,i+1)
            
            rem = sum - k
            
            if (rem in prevSumMap):
                len = i - prevSumMap[rem]
                maxLen = max(maxLen,len)
            
            if (sum not in prevSumMap):
                prevSumMap[sum] = i
            
        return maxLen
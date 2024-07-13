'''Given an array arr[], with index ranging from 0 to n-1, select any two indexes, i and j such that i < j .
 From the subarray arr[i...j], select the two minimum numbers and add them, you will get the score for that subarray.
 Return the maximum possible score across all the subarrays of array arr[].'''

class Solution:
    def pairWithMaxSum(self, arr, N):
        min1 = arr[0]
        maxsum = float('-inf')
        for i in range(1, N) :
            min2, min1 = min1,arr[i]
            tsum = min1 + min2
            if maxsum < tsum :
                maxsum = tsum
        
        return maxsum
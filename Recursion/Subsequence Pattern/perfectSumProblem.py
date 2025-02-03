'''Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array 
whose sum is equal to the given target.
https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1'''

# This solution takes O(2^n) time complexity and O(n) space complexity and gives TLE for large inputs
def cntSubseqSum(i, arr, subseqSum, target):
    if subseqSum > target:
        return 0
    if i == len(arr):
        if subseqSum == target:
            return 1
        return 0
    
    subseqSum += arr[i]
    l = cntSubseqSum(i+1, arr, subseqSum, target)
    subseqSum -= arr[i]
    r = cntSubseqSum(i+1, arr, subseqSum, target)
    return l+r

class Solution:
    def perfectSum(self, arr, target):
        res = cntSubseqSum(0, arr, 0, target)
        return res
    

# DP solution
# This solution takes O(n*target) time complexity and O(n*target) space complexity
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)

        dp = [[-1 for _ in range(target+1)] for _ in range(n)]
        
        def solve(n, k):
            if n == 0:
                if k == 0 and arr[n] == 0: return 2
                if arr[n] == k or k == 0:
                    return 1
                return 0
            
            if dp[n][k] == -1:
                notTake = solve(n-1, k)
                take = 0
                if arr[n] <= k:
                    take = solve(n-1, k-arr[n]) 
                
                dp[n][k] = (notTake + take)
            
            return dp[n][k]
        
        return solve(n-1, target)
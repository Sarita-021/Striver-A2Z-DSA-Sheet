'''Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

https://leetcode.com/problems/subsets-ii/description/ '''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def uniqueSubsets(idx, lst):
            res.append(lst[:])
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                lst.append(nums[i])
                uniqueSubsets(i+1, lst)
                lst.pop()
                
        uniqueSubsets(0, [])
        return res
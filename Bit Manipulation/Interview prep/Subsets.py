'''Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
https://leetcode.com/problems/subsets/'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = 2 << len(nums)-1
        for i in range(subsets):
            lst = []
            for j in range(len(nums)):
                if i & (1 << j):
                    lst.append(nums[j])
            res.append(lst)
        
        return res
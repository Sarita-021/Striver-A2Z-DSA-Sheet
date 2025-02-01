'''Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
https://leetcode.com/problems/subsets/description/'''


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generateSubsets(i, s, f):
            if len(s) == i:
                res.append(f[:])
                return 
            
            f.append(s[i])

            generateSubsets(i+1, s, f)

            f.pop()
            generateSubsets(i+1, s, f)

        generateSubsets(0, nums, [])
        return res

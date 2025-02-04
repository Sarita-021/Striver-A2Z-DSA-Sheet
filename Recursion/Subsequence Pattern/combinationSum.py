'''Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations 
for the given input.
https://leetcode.com/problems/combination-sum/description/'''


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def generateCombinationSum(idx, lst, target, n):
            if target < 0:
                return 
            if idx >= n:
                if target == 0:
                    res.append(lst[:])
                return
            
            if candidates[idx] <= target:
                lst.append(candidates[idx])
                generateCombinationSum(idx, lst, target-candidates[idx], n)
                lst.pop()

            generateCombinationSum(idx+1, lst, target, n)
        
        generateCombinationSum(0, [], target, n)
        return res
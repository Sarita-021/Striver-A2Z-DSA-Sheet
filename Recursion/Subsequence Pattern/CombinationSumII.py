'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in 
candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
https://leetcode.com/problems/combination-sum-ii/description/ '''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def findS(idx, lst, target):
            if target == 0:
                res.append(lst[:])
                return 
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                lst.append(candidates[i])
                findS(i+1, lst, target-candidates[i])
                lst.pop()
        findS(0, [], target)
        return res
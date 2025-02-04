'''Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.
https://leetcode.com/problems/combination-sum-iii/ '''

from typing import List

# Optimized solution

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, target, path):
            # If we have selected k numbers
            if len(path) == k:
                if target == 0:
                    res.append(path[:])  # Store a copy of the valid combination
                return
            
            for i in range(start, 10):  # Iterate through numbers 1 to 9
                if i > target:  # Prune unnecessary recursion
                    break
                path.append(i)
                backtrack(i + 1, target - i, path)  # Move forward to avoid duplicates
                path.pop()  # Backtrack to explore other paths
        
        backtrack(1, n, [])
        return res



# Less optimized solution

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < 3:
            return []
        res = []
        def combSum(lst, c, s):
            if s > n:
                return
            if len(lst) == k:
                if s == n:
                    res.append(lst[:])
                return
            
            if c < 10:
                lst.append(c)
                combSum(lst, c+1, s+c)
                lst.pop()
                combSum(lst, c+1, s)

        combSum([], 1, 0)
        return res
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
https://leetcode.com/problems/generate-parentheses/description/ '''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openP, closeP, st):
            if openP == closeP and openP + closeP == n*2:
                res.append(st)
                return
            
            if openP < n:
                dfs(openP+1, closeP, st+'(')
            
            if closeP < openP:
                dfs(openP, closeP+1, st+')')

        dfs(0, 0, '')
        return res
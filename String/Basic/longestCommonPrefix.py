'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        n = len(strs[0])
        ans = ""
        for i in range(n):
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
            else :
                return ans
        return ans
        
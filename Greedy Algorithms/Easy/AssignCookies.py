'''Assume you are an awesome parent and want to give your children some cookies. But, you should give each child
at most one cookie.
https://leetcode.com/problems/assign-cookies/description/'''

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        m = len(g)
        n = len(s)
        l = r = 0
        while l < n and r < m:
            if g[r] <= s[l]:
                r += 1
            l += 1
        return r
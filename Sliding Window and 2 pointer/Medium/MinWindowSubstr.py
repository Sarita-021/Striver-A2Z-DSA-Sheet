'''Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
https://leetcode.com/problems/minimum-window-substring/'''

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        minlen = len(s)+1
        l = r = cnt = 0
        freqcnt = defaultdict(int)
        for i in t:
            freqcnt[i] += 1

        si = -1
        for r in range(len(s)):
            if freqcnt[s[r]] > 0: 
                cnt += 1
            freqcnt[s[r]] -= 1
            
            while cnt == len(t):
                if r-l+1 < minlen:
                    minlen = r-l+1
                    si = l
                freqcnt[s[l]] += 1
                if freqcnt[s[l]] > 0:
                    cnt -= 1
                l += 1
        return s[si:si+minlen] if si != -1 else ''
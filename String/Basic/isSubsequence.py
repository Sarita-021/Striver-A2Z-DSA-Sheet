'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        if len(s) == 0:
            return True
        for i in t:
            if i == s[p]:
                p += 1
                if p == len(s):
                    return True
        return False
        

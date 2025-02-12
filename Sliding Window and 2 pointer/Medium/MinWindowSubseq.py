'''
https://leetcode.com/problems/minimum-window-subsequence/'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
    
        minlen = len(s) + 1
        r, si = 0, -1
        i = 0
        
        for r in range(len(s)):
            if s[r] == t[i]: 
                i += 1
            
            # Found a valid subsequence
            if i == len(t):
                l = r
                i -= 1  # Move back through t
                
                # Shrink window from the right to left
                while i >= 0:
                    if s[l] == t[i]:
                        i -= 1
                    l -= 1  # Move left
                
                l += 1  # Adjust to point to the start of valid subsequence
                
                # Update the minimum window found
                if minlen > r - l + 1:
                    si = l
                    minlen = r - l + 1
            
        return s[si:si+minlen] if si != -1 else ''

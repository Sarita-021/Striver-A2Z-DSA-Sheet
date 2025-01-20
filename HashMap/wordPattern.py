'''Given a pattern and a string s, find if s follows the same pattern.

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        n = len(pattern)
        st = e = 0
        for i in range(n):
            k = pattern[i]
            while e < len(s) and s[e] != ' ':
                e += 1
            v = s[st:e]
            print(k,v)
            if (k not in mp.keys()) and (v not in mp.values()):
                mp[k] = v
            elif k not in mp.keys() or mp[k] != v:
                return False
            st = e = e+1
        e -= 1
        
        return True if e == len(s) else False
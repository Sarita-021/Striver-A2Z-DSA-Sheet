'''Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        n = len(s)
        for i in range(n):
            k, v = s[i], t[i]
            if (k not in mp.keys()) and (v not in mp.values()):
                mp[k] = v
            elif k not in mp.keys() or mp[k] != v:
                return False
        
        return True
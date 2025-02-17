'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Step 1: Build LPS Array
        def computeLPS(needle):
            lps = [0] * len(needle)
            j = 0  # length of previous longest prefix suffix
            for i in range(1, len(needle)):
                while j > 0 and needle[i] != needle[j]:
                    j = lps[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        lps = computeLPS(needle)
        i = j = 0  # Pointers for haystack and needle
        
        # Step 2: Search `needle` in `haystack`
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  # Found match
            else:
                if j > 0:
                    j = lps[j - 1]  # Move `j` to previous LPS
                else:
                    i += 1  # Move `i` normally
        
        return -1  # No match found

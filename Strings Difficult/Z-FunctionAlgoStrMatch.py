'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        concat = needle + "$" + haystack  # Combine strings with a delimiter
        Z = [0] * len(concat)
        
        # Step 1: Build Z-array
        l, r, n = 0, 0, len(concat)
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and concat[Z[i]] == concat[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1
        
        # Step 2: Find `needle` in `haystack`
        for i in range(len(needle) + 1, len(concat)):  # Start after "needle$"
            if Z[i] == len(needle):
                return i - len(needle) - 1  # Adjust index for haystack
        
        return -1  # No match found
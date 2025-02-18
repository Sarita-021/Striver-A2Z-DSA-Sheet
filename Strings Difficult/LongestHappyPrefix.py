'''A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.
https://leetcode.com/problems/longest-happy-prefix/description/'''


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        j = 0  # Length of the longest prefix which is also a suffix

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]  # Move back in the LPS array
            
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        return s[:lps[-1]]  # The longest happy prefix
'''Given a string s, find the length of the longest substring without repeating characters.
https://leetcode.com/problems/longest-substring-without-repeating-characters/'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            output = max(output,r-l+1)
        return output   
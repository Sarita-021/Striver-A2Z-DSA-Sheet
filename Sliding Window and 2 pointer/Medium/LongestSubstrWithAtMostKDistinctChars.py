'''Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
Input: s = "eceba", k = 2 Output: 3 Explanation: The substring is "ece" with length 3.
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        left = 0
        max_len = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

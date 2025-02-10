'''You are given a string s and an integer k. You can choose any character of the string and change it to any other u
ppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
https://leetcode.com/problems/longest-repeating-character-replacement/description/'''

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        char_count = defaultdict(int)
        
        for r in range(len(s)):
            char_count[s[r]] += 1
            max_freq = max(max_freq, char_count[s[r]])  # Most frequent character count
            
            # If changes needed (window size - max_freq) exceed k, shrink window
            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1  # Move left pointer to shrink window
        
        return len(s) - l  # Maximum valid window size
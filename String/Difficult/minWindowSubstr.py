'''Given two strings s and t of lengths m and n respectively, return the minimum window substring
 of s such that every character in t (including duplicates) is included in the window. 
 If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

https://leetcode.com/problems/minimum-window-substring/'''

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) : 
            return ''

        res = ''
        char_cnt = defaultdict(int)
        for c in t:
            char_cnt[c] += 1

        l = 0
        min_window = (0, len(s)+1)
        target_char_cnt = len(t)

        for r, ch in enumerate(s):
            if char_cnt[ch] > 0:
                target_char_cnt -= 1
            char_cnt[ch] -= 1

            if target_char_cnt == 0:
                while True:
                    char_at_start = s[l]
                    if char_cnt[char_at_start] == 0:
                        break
                    char_cnt[char_at_start] += 1
                    l += 1
                
                if r - l < min_window[1] - min_window[0]:
                    min_window = [ l, r]
                
                char_cnt[s[l]] += 1
                target_char_cnt += 1
                l += 1
        
        return '' if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]


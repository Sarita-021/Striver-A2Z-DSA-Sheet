'''Given a string s, find the length of the longest 
substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
 '''
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substr = ''
        for i in s:
            while i in substr :
                substr = substr[1:]
            
            substr += i
            longest = max(longest, len(substr))
        return longest
        
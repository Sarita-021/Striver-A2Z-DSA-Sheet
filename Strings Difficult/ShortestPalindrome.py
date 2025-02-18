'''You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

Input: s = "aabba"
Output: "abbaabba"     
https://leetcode.com/problems/shortest-palindrome/'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Construct a new string with a delimiter
        temp = s + "#" + s[::-1]
        
        # Compute the KMP prefix table (LPS array)
        lps = [0] * len(temp)
        
        for i in range(1, len(temp)):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        
        # The last value in LPS gives the longest palindromic prefix
        longest_palindrome_len = lps[-1]
        
        # Add the remaining characters in reverse order to form the shortest palindrome
        return s[longest_palindrome_len:][::-1] + s

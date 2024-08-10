'''Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""

        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        start, end = 0, 0

        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expandAroundCenter(s, i, i)
            # Check for even-length palindromes
            even_palindrome = expandAroundCenter(s, i, i + 1)

            # Get the longer of the two palindromes
            longer_palindrome = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome

            # Update the start and end pointers if we found a longer palindrome
            if len(longer_palindrome) > end - start:
                start = i - (len(longer_palindrome) - 1) // 2
                end = i + len(longer_palindrome) // 2

        return s[start:end + 1]
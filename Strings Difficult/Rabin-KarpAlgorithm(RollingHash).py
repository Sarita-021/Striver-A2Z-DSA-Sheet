'''Given two strings text and pattern, find the first index where pattern exactly matches with any substring of text. 
Return -1 if pattern doesn't exist as a substring in text.
geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/1'''

class Solution:
    def findMatching(self, text, pattern):
        if not pattern or not text or len(text) < len(pattern):
            return -1

        m, n = len(text), len(pattern)
        base, mod = 31, 10**9 + 7  # Hash base and large prime modulus

        # Compute hash of pattern and first window of text
        pattern_hash = 0
        text_hash = 0
        power = 1  # Stores base^(n-1)

        for i in range(n):
            pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
            text_hash = (text_hash * base + ord(text[i])) % mod
            if i < n - 1:
                power = (power * base) % mod

        # Check first window
        if pattern_hash == text_hash and text[:n] == pattern:
            return 0

        # Rolling hash for remaining windows
        for i in range(n, m):
            text_hash = (text_hash - ord(text[i - n]) * power) % mod
            text_hash = (text_hash * base + ord(text[i])) % mod
            
            if text_hash == pattern_hash and text[i - n + 1:i + 1] == pattern:
                return i - n + 1
        
        return -1
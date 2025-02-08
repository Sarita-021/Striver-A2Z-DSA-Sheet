'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
https://leetcode.com/problems/word-break/description/'''


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))  

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
    
#   Recursive solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        memo = {}
        def canBreak(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]

            for end in range(start + 1, n + 1):
                if s[start:end] in wordDict and canBreak(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return canBreak(0)
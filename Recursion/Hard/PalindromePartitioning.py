'''Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
https://leetcode.com/problems/palindrome-partitioning/description/'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def partitionHelper(index: int):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    partitionHelper(i + 1)
                    path.pop()
        
        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        partitionHelper(0)
        return res


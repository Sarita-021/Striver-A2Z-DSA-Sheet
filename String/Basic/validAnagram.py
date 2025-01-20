'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.'''

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
'''OR'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for x in s:
            count[x] += 1

        for x in t:
            count[x] -= 1
            
        for val in count.values():
            if val != 0:
                return False
        
        return True
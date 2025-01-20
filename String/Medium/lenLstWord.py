'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.'''
 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        while s[i] == ' ':
            i -= 1
        
        l = 0
        while i >= -len(s) and s[i] != ' ':
            l += 1
            i -= 1

        return l
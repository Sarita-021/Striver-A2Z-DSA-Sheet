'''Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
https://leetcode.com/problems/valid-parenthesis-string/'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        mn = 0
        mx = 0
        for i in s:
            if i == '(':
                mn += 1
                mx += 1
            elif i == ')':
                mn -= 1
                mx -= 1
            else:
                mn -= 1
                mx += 1 
            if mn < 0:
                mn = 0
            if mx < 0:
                return False
                 
        return mn == 0
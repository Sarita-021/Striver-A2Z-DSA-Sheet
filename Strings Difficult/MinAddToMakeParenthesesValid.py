'''You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        missingClose = missingOpen = 0  # Tracks unclosed '(' and unmatched ')'
        
        for char in s:
            if char == '(':
                missingClose += 1  # Needs a closing bracket
            elif char == ')' and missingClose:
                missingClose -= 1  # Matches an existing '('
            else:
                missingOpen += 1  # Unmatched ')', needs an opening bracket
        
        return missingClose + missingOpen  # Total missing brackets
    